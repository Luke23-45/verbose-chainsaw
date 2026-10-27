"""PDF readers, in strict order of trust.

text_reader -> table_reader -> ocr_reader. The method used for a value
is always recorded in its provenance; a reader never silently replaces
another reader's output.
"""
