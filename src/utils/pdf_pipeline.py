#!/usr/bin/env python3
"""
pdf_pipeline.py
===============
Robust PDF Page Extraction & Rasterization Pipeline.

Takes a JSON task configuration and extracts selected pages as new PDFs
or high-resolution images (PNG/JPEG).

Author: Architecture & Engineering Team
Python Version: >= 3.8
Dependencies: pymupdf
"""

import os
import sys
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Union, Optional
from dataclasses import dataclass, field

try:
    import pymupdf  # PyMuPDF
except ImportError:
    print("[ERROR] PyMuPDF is not installed. Please run: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("PDFPipeline")


# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------
@dataclass
class TaskConfig:
    task_id: str
    src: Path
    pages_spec: Any
    output_form: str
    output_dir: Path
    image_format: str = "png"
    dpi: int = 200
    custom_name: Optional[str] = None


@dataclass
class TaskResult:
    task_id: str
    success: bool
    message: str
    output_files: List[Path] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Component 1: Page Range Resolver
# ---------------------------------------------------------------------------
class PageResolver:
    """
    Parses flexible page configuration patterns into 0-based page index lists.
    Supported inputs (1-based from user perspective):
      - "all"
      - "3-10"
      - "5-" (page 5 to end)
      - "-5" (page 1 to 5)
      - [1, 2, 5]
      - "1, 3-5, 8"
      - {"range": "3-10"}
      - {"list": [1, 2, 5]}
    """

    @staticmethod
    def _parse_range_token(token: str, total_pages: int) -> List[int]:
        token = token.strip()
        if not token:
            return []

        if "-" in token:
            parts = token.split("-", maxsplit=1)
            start_str, end_str = parts[0].strip(), parts[1].strip()

            start = int(start_str) if start_str else 1
            end = int(end_str) if end_str else total_pages

            if start < 1:
                raise ValueError(f"Page numbers must be >= 1. Received: {start}")
            if end > total_pages:
                raise ValueError(f"Requested page {end} exceeds total pages ({total_pages}).")
            if start > end:
                raise ValueError(f"Invalid range: {start}-{end} (start is greater than end).")

            # Convert 1-based inclusive range to 0-based indices
            return list(range(start - 1, end))
        else:
            page = int(token)
            if page < 1 or page > total_pages:
                raise ValueError(f"Page {page} out of bounds (1 to {total_pages}).")
            return [page - 1]

    @classmethod
    def resolve(cls, pages_spec: Any, total_pages: int) -> List[int]:
        if pages_spec is None or pages_spec == "all":
            return list(range(total_pages))

        indices: List[int] = []

        # Case 1: Dictionary configuration
        if isinstance(pages_spec, dict):
            # Check for "list"
            if "list" in pages_spec and isinstance(pages_spec["list"], list):
                for item in pages_spec["list"]:
                    if isinstance(item, int):
                        if 1 <= item <= total_pages:
                            indices.append(item - 1)
                        else:
                            raise ValueError(f"Page {item} out of range (1 to {total_pages}).")
                    elif isinstance(item, str):
                        indices.extend(cls._parse_range_token(item, total_pages))

            # Check for "range"
            if "range" in pages_spec:
                r_val = pages_spec["range"]
                if isinstance(r_val, str):
                    for sub in r_val.split(","):
                        indices.extend(cls._parse_range_token(sub, total_pages))
                elif isinstance(r_val, (list, tuple)) and len(r_val) == 2:
                    indices.extend(cls._parse_range_token(f"{r_val[0]}-{r_val[1]}", total_pages))

        # Case 2: Direct list of pages/ranges
        elif isinstance(pages_spec, list):
            for item in pages_spec:
                if isinstance(item, int):
                    if 1 <= item <= total_pages:
                        indices.append(item - 1)
                    else:
                        raise ValueError(f"Page {item} out of range (1 to {total_pages}).")
                elif isinstance(item, str):
                    indices.extend(cls._parse_range_token(item, total_pages))

        # Case 3: Comma-delimited string (e.g. "1, 3-5, 8")
        elif isinstance(pages_spec, str):
            for token in pages_spec.split(","):
                indices.extend(cls._parse_range_token(token, total_pages))

        else:
            raise TypeError(f"Unsupported 'pages' configuration format: {type(pages_spec)}")

        # Deduplicate while preserving sequence
        seen = set()
        deduped = []
        for idx in indices:
            if idx not in seen:
                seen.add(idx)
                deduped.append(idx)

        if not deduped:
            raise ValueError("No valid pages were resolved from the provided specification.")

        return deduped


# ---------------------------------------------------------------------------
# Component 2: Execution Engine
# ---------------------------------------------------------------------------
class PDFProcessorEngine:
    """Executes the extraction tasks using PyMuPDF."""

    @staticmethod
    def extract_pdf(
        doc: pymupdf.Document,
        page_indices: List[int],
        output_path: Path
    ) -> Path:
        """Extracts specified pages into a new compact PDF."""
        new_doc = pymupdf.open()
        for idx in page_indices:
            new_doc.insert_pdf(doc, from_page=idx, to_page=idx)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        # garbage=4: remove unused objects; deflate=True: compress streams
        new_doc.save(str(output_path), garbage=4, deflate=True)
        new_doc.close()
        return output_path

    @staticmethod
    def extract_images(
        doc: pymupdf.Document,
        page_indices: List[int],
        output_dir: Path,
        base_name: str,
        img_format: str = "png",
        dpi: int = 200
    ) -> List[Path]:
        """Renders specified pages as images with DPI scaling."""
        output_dir.mkdir(parents=True, exist_ok=True)
        generated_files: List[Path] = []
        is_jpeg = img_format.lower() in ("jpg", "jpeg")

        for idx in page_indices:
            human_page_num = idx + 1
            page = doc.load_page(idx)

            # Prevent black background on JPEG by omitting alpha channel
            pix = page.get_pixmap(dpi=dpi, alpha=not is_jpeg)

            file_name = f"{base_name}_page_{human_page_num:04d}.{img_format.lower()}"
            file_path = output_dir / file_name

            pix.save(str(file_path))
            generated_files.append(file_path)

        return generated_files


# ---------------------------------------------------------------------------
# Component 3: Pipeline Orchestrator
# ---------------------------------------------------------------------------
class PDFPipeline:
    """Orchestrates configuration validation, file handling, and batch execution."""

    def __init__(self, default_output_dir: Path = Path("output")):
        self.default_output_dir = default_output_dir

    def parse_task(self, task_id: str, raw_config: Dict[str, Any]) -> TaskConfig:
        if not isinstance(raw_config, dict):
            raise ValueError(f"Task '{task_id}' definition must be an object/dict.")

        if "src" not in raw_config:
            raise KeyError(f"Task '{task_id}' is missing mandatory 'src' field.")

        src = Path(raw_config["src"]).expanduser().resolve()
        if not src.is_file():
            raise FileNotFoundError(f"Source file not found for task '{task_id}': {src}")

        output_form = raw_config.get("output_form", "pdf").strip().lower()
        # Normalize forms
        if output_form in ("images", "image", "img", "png", "jpg", "jpeg"):
            form_type = "images"
            img_format = "jpg" if output_form in ("jpg", "jpeg") else raw_config.get("format", "png")
        elif output_form in ("pdf", "pdf_extracted"):
            form_type = "pdf"
            img_format = "png"
        else:
            raise ValueError(f"Unsupported output_form '{output_form}' in task '{task_id}'")

        # Destination directory
        if "output_dir" in raw_config:
            out_dir = Path(raw_config["output_dir"]).expanduser().resolve()
        else:
            out_dir = (self.default_output_dir / task_id).resolve()

        return TaskConfig(
            task_id=task_id,
            src=src,
            pages_spec=raw_config.get("pages"),
            output_form=form_type,
            output_dir=out_dir,
            image_format=img_format,
            dpi=int(raw_config.get("dpi", 200)),
            custom_name=raw_config.get("output_name")
        )

    def execute_task(self, task: TaskConfig) -> TaskResult:
        logger.info(f"==> Processing Task: [{task.task_id}] (Source: {task.src.name})")

        doc = None
        try:
            doc = pymupdf.open(str(task.src))
            total_pages = doc.page_count
            logger.info(f"    Document loaded: {total_pages} total pages.")

            # Resolve page indices
            page_indices = PageResolver.resolve(task.pages_spec, total_pages)
            logger.info(f"    Pages selected ({len(page_indices)}): {[p + 1 for p in page_indices]}")

            generated_files: List[Path] = []

            if task.output_form == "pdf":
                file_name = f"{task.custom_name or task.task_id}.pdf"
                dest_file = task.output_dir / file_name
                output_pdf = PDFProcessorEngine.extract_pdf(doc, page_indices, dest_file)
                generated_files.append(output_pdf)
                logger.info(f"    Saved PDF -> {output_pdf}")

            elif task.output_form == "images":
                base_name = task.custom_name or task.task_id
                img_files = PDFProcessorEngine.extract_images(
                    doc=doc,
                    page_indices=page_indices,
                    output_dir=task.output_dir,
                    base_name=base_name,
                    img_format=task.image_format,
                    dpi=task.dpi
                )
                generated_files.extend(img_files)
                logger.info(f"    Generated {len(img_files)} images -> {task.output_dir}")

            return TaskResult(
                task_id=task.task_id,
                success=True,
                message=f"Successfully extracted {len(page_indices)} pages.",
                output_files=generated_files
            )

        except Exception as e:
            logger.error(f"    [FAIL] Task '{task.task_id}' failed: {e}", exc_info=False)
            return TaskResult(
                task_id=task.task_id,
                success=False,
                message=str(e),
                output_files=[]
            )
        finally:
            if doc is not None:
                doc.close()

    def run_from_config(self, json_path: Union[str, Path]) -> List[TaskResult]:
        config_path = Path(json_path).expanduser().resolve()
        if not config_path.is_file():
            raise FileNotFoundError(f"Configuration file does not exist: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            try:
                raw_json = json.load(f)
            except json.JSONDecodeError as err:
                raise ValueError(f"Malformed JSON configuration: {err}") from err

        if not isinstance(raw_json, dict):
            raise ValueError("Root configuration must be a JSON object mapping task IDs to specifications.")

        results: List[TaskResult] = []
        logger.info(f"Loaded config from {config_path.name} with {len(raw_json)} task(s).")

        for task_id, task_data in raw_json.items():
            try:
                task_config = self.parse_task(task_id, task_data)
                result = self.execute_task(task_config)
                results.append(result)
            except Exception as e:
                logger.error(f"Failed to initialize task '{task_id}': {e}")
                results.append(TaskResult(task_id=task_id, success=False, message=str(e)))

        return results


# ---------------------------------------------------------------------------
# CLI Entry Point & Summary Reporter
# ---------------------------------------------------------------------------
def print_summary(results: List[TaskResult]):
    print("\n" + "=" * 60)
    print("                     EXECUTION SUMMARY")
    print("=" * 60)
    success_count = sum(1 for r in results if r.success)
    failed_count = len(results) - success_count

    for r in results:
        status = "PASSED" if r.success else "FAILED"
        print(f"[{status}] Task ID : {r.task_id}")
        print(f"         Status  : {r.message}")
        if r.output_files:
            print(f"         Outputs : {len(r.output_files)} file(s) generated")
            for f in r.output_files[:3]:  # print first 3 as preview
                print(f"                   - {f}")
            if len(r.output_files) > 3:
                print(f"                   ... and {len(r.output_files) - 3} more.")
        print("-" * 60)

    print(f"Total: {len(results)} | Succeeded: {success_count} | Failed: {failed_count}")
    print("=" * 60 + "\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract PDF pages or render to images based on JSON task specifications."
    )
    parser.add_argument(
        "config_json",
        type=str,
        help="Path to the JSON task configuration file."
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default="output",
        help="Default base output directory if not specified in task JSON."
    )
    args = parser.parse_args()

    pipeline = PDFPipeline(default_output_dir=Path(args.output_dir))

    try:
        results = pipeline.run_from_config(args.config_json)
        print_summary(results)

        # Non-zero exit code if all tasks failed
        if results and all(not r.success for r in results):
            sys.exit(1)

    except Exception as e:
        logger.critical(f"Pipeline execution aborted: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()