"""One module per statement. A parser returns candidate values with
provenance (file, page, method, confidence); it never writes the panel
directly. Parsers are filled in one statement at a time, against real
pages, and tested on fixture pages — not on live PDFs.
"""
