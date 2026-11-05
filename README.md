# E. coli PBP3/FtsI conformation-aware virtual screening — supporting data

This repository contains original computational compound-library and QSAR prediction outputs supporting the manuscript **“Reliability-aware QSAR and conformation-aware virtual screening of Escherichia coli PBP3-targeting candidates with resistance-context mapping.”**

## Included research data

- `01_Compound_Library/PBP3_2000_Compound_Library.csv`: 2,000 CyberAIDD/CyberX-Discovery generated compounds with source `pref_name` identifiers, canonical SMILES, and calculated physicochemical descriptors (source file `QBA_20260711.csv`).
- `01_Compound_Library/PBP3_2000_ID_SMILES.csv`: convenient two-column identifier and canonical-SMILES index.
- `02_QSAR_Data/PBP3_2000_QSAR_Predictions.csv`: 2,000 predictions from an anti-*Staphylococcus aureus* whole-cell MIC QSAR prescreen, including reliability estimates, consensus predictions, and rank (source file `QBA_2000_QSAR_predictions.csv`).

### Verification

Library entries: **2,000**. Unique compound IDs: **2,000**. Unique canonical SMILES: **2,000**. ID/SMILES mismatches across the two data files: **0**. Missing SMILES: **0**. QSAR reliability: **259 High, 785 Moderate, 956 Low**. The source library's empty `mol_formula` fields remain unfilled.

### Scope of interpretation

These are **generated chemical structures and computational predictions**, not experimentally verified PBP3 inhibitors. Whole-cell anti-*S. aureus* predictions should not be interpreted as measured *E. coli* antibacterial potency, PBP3 binding affinity, target engagement, or enzyme inhibition.

This **library and prediction release is not a complete reproduction package**: curated QSAR training records, model-training scripts and fitted model binaries, the complete docking/pose outputs, and MD/MM-GBSA input files and trajectories are not provided in this initial deposit. These may be added as verified separate deposits.

### Sharing and licensing

This repository is being prepared privately for scientific-reviewer reproducibility. No data or code license is assigned. Before making this repository public, verify permission to redistribute CyberAIDD/CyberX-Discovery generated outputs and any third-party material. Do not assume unrestricted reuse from the absence of a license.

### Citation

Please cite the associated manuscript when published. A formal archive DOI has not yet been assigned.
