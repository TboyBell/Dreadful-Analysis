# Release Notes

**Package version:** v1.0-frozen-phase3

## Status
Phase 2 and Phase 3 have passed independent audit and are frozen.

## Integrity
No approved analytical file (cleaning script, cleaned dataset, Phase 3
script, or any of Figures B/C/D) was modified, regenerated, or recalculated
during packaging. This was a file-management task only. Validation
performed before delivery (re-running `phase3_frozen.py` against the
packaged cleaned CSV) confirmed byte-identical figures and unchanged
numerical results — see the final chat response for the full validation
log.

## For Phase 4
Phase 4 (modelling) must use this package as its starting point:
- Cleaned data: `02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`
- Frozen research questions and effect-size findings:
  `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`
- Two of five total report figure slots remain unallocated for modelling
  results (three are used by Figures B, C, D).

## Do not use
Anything inside `99_Superseded_File_List/Archive_Do_Not_Use/` is retained
for traceability only and must not be used in the report or in Phase 4.
See `99_Superseded_File_List/SUPERSEDED_FILES.md` for why each file was
superseded.
