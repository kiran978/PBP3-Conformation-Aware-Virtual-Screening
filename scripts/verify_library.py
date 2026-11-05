#!/usr/bin/env python3
"""Verify the original 2000-compound PBP3 library and QSAR predictions."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(relative_path):
    with (ROOT / relative_path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

source = read("01_Compound_Library/PBP3_2000_Compound_Library.csv")
index = read("01_Compound_Library/PBP3_2000_ID_SMILES.csv")
predictions = read("02_QSAR_Data/PBP3_2000_QSAR_Predictions.csv")
assert len(source) == len(index) == len(predictions) == 2000, "Expected 2,000 records per file"
molecules = {row["pref_name"]: row["canonical_smiles"] for row in source}
assert len(molecules) == 2000, "Duplicate or missing compound IDs"
assert all(molecules.values()) and len(set(molecules.values())) == 2000, "Missing or duplicate SMILES"
for record in index + predictions:
    assert molecules.get(record["Compound_ID"]) == record["Canonical_SMILES"], "SMILES mismatch"
reliability = Counter(record["Reliability"] for record in predictions)
assert reliability == {"High": 259, "Moderate": 785, "Low": 956}, reliability
print("PASS: 2000 compounds; 2000 unique IDs and structures; zero ID/SMILES mismatches")
print("Prediction reliability:", dict(reliability))
