# Phase 2 — Cleaning (FROZEN)

## Purpose
Converts the raw, two-region-block UCI file into a single, validated,
analysis-ready CSV: deriving column names from the file's own header
(verified, not hardcoded), splitting the two embedded region blocks,
repairing one structurally malformed record, standardising whitespace and
types, and adding `Region` and `date` columns.

## How to run
```
python3 clean_forest_fires.py --raw-path <path-to-raw-csv> --output-path <output-path>
```
Both arguments default to the original project's file layout if omitted.

## Required input
The original raw file from `01_Original_Data/algerian_forest_fires_dataset.zip`
(`Algerian_forest_fires_dataset_UPDATE.csv`, extracted).

## Generated output
`Algerian_forest_fires_dataset_CLEANED.csv`

## Final dataset shape
**244 records × 17 attributes** (14 original + `Region` + `date` +
`record_repaired`).

## Repaired-record assumption
One record (14 July 2012, Sidi-Bel Abbes) had a missing comma merging two
numeric fields. It was reconstructed as the *most plausible* split (DC=14.6,
ISI=9) based on column order and both values falling within the normal range
observed elsewhere in the dataset — this is a reconstruction, not a verified
correction, since the original comma is unrecoverable with certainty.

## Repaired record is explicitly flagged
The `record_repaired` column is `True` for exactly one record and `False`
for all 243 others, so it can be isolated or excluded in any later analysis.

## Validation checks performed (enforced by assertion, not just printed)
- 244 total records
- 0 missing values
- 0 duplicate rows
- Exactly two region labels, 122 records each
- Exactly two class labels (`fire`, `not fire`)
- All dates within the documented 1 June – 30 September 2012 window

## Audit status
**Phase 2 passed independent audit** and is frozen. Do not alter
`clean_forest_fires.py` or `Algerian_forest_fires_dataset_CLEANED.csv`.
