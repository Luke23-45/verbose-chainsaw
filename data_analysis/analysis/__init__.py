"""Publication analysis pipeline for the MPS_RD value-relevance study.

Regenerates every thesis figure and table for the value-relevance question
(EPS/BVPS association with market price before and after the Nepalese banking
consolidation wave, FY2076/77-FY2081/82, five commercial bank series) from the
frozen data_extract outputs, per proposal section 07_methodology.

Data flow is strictly one-way: loaders -> dataset -> assets -> render.  Assets
never touch the filesystem; they receive an AnalysisDataset.

Entry point (run from data_analysis/):
    python -m analysis.scripts.generate --check
    python -m analysis.scripts.generate
    python -m analysis.scripts.verify
"""
