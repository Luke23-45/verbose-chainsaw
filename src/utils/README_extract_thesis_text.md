# Merge thesis chapter sources into a `.txt` file

Run from the repository root:

```powershell
python src/utils/extract_thesis_text.py
```

The script reads every `chapter_*.tex` file from
`src/thesis/chapters/`, sorts the files by filename (chapter number), and
concatenates their contents verbatim into
`src/thesis/chapters/all_chapters.txt`. It adds a filename heading before each
chapter. LaTeX source commands are preserved; the script does not build the
thesis or convert the source to rendered prose.

To choose another output path:

```powershell
python src/utils/extract_thesis_text.py -o "path\to\chapters.txt"
```
