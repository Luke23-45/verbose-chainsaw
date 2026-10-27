"""Deterministic extraction of the 30 audited bank reports.

Public entry point is the CLI (``python -m data_extract.cli ...``).
Nothing in this package reads a PDF for the analysis stage; analysis
reads only ``output/tidy/bank_year_panel.csv``.
"""

__version__ = "0.1.0"
