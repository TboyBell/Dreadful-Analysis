# Release Notes

**Package version:** v2.0-frozen-phase4

## Status

Phases 1, 2, 3 and 4 have passed their required audit gates and are frozen.

- Phase 2 cleaning: passed and frozen.
- Phase 3 EDA: passed and frozen.
- Phase 4A design: **PASS — Freeze Phase 4A and authorise Phase 4B**.
- Phase 4B computation: **PASS WITH MINOR NON-BLOCKING CORRECTIONS**.
- Phase 4 final status: analytically accepted and frozen after non-analytical package cleanup.

## Integrity

The final release begins from the original `DAM140_Phases_1_to_3_Frozen.zip` bytes. All prior analytical, source, data, figure and prior audit-decision files were preserved byte-for-byte. The package-level `AUDIT_STATUS.md`, `MASTER_MANIFEST.csv`, `CHECKSUMS_SHA256.txt` and this release note were updated solely to record Phase 4 and final-release controls.

Phase 4 was integrated from the audited `04_Phase_4_Modelling_Frozen/` folder. No model, prediction, metric, coefficient, permutation-importance result, RQ2 result or figure was recalculated during final assembly. The original code-generated Figure 4 and Figure 5 bytes were preserved.

## Interpretation boundary

`Classes` is an FWI/FFMC-derived class designation, not independently observed wildfire incidence. Phase 4 evaluates reproduction of this designation and must not be described as wildfire forecasting or real-fire detection. The exact class thresholds are undocumented.

## Files permitted for final-report writing

The following frozen files are the principal authorised report sources:

- `02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`
- `03_Phase_3_EDA_Frozen/fig_B_weather_by_class.png`
- `03_Phase_3_EDA_Frozen/fig_C_monthly_class_proportion.png`
- `03_Phase_3_EDA_Frozen/fig_D_fwi_weekly_trend.png`
- `04_References/BOOK_Chapter_Springer_ABID.pdf`
- `04_Phase_4_Modelling_Frozen/PHASE4_FROZEN_SUMMARY.md`
- `04_Phase_4_Modelling_Frozen/fold_metrics.csv`
- `04_Phase_4_Modelling_Frozen/metric_summary.csv`
- `04_Phase_4_Modelling_Frozen/pooled_oof_metrics.csv`
- `04_Phase_4_Modelling_Frozen/pooled_confusion_matrices.csv`
- `04_Phase_4_Modelling_Frozen/model_selection_decision.json`
- `04_Phase_4_Modelling_Frozen/rain_binary_sensitivity_metrics.csv`
- `04_Phase_4_Modelling_Frozen/boundary_gap_sensitivity_metrics.csv`
- `04_Phase_4_Modelling_Frozen/logistic_full_data_coefficients.csv`
- `04_Phase_4_Modelling_Frozen/permutation_importance_summary.csv`
- `04_Phase_4_Modelling_Frozen/rq2_specification_results.csv`
- `04_Phase_4_Modelling_Frozen/rq2_interaction_sensitivity.csv`
- `04_Phase_4_Modelling_Frozen/fig_4_rq1_lomo_balanced_accuracy.png`
- `04_Phase_4_Modelling_Frozen/fig_5_rq1_logistic_odds_ratios.png`

The `final_report_use` column in `MASTER_MANIFEST.csv` is controlling. Detailed code, environments, predictions, repeat-level importance values, logs, manifests and audit records are supporting evidence rather than report-ready conclusions.

## Do not use

Anything inside `99_Superseded_File_List/Archive_Do_Not_Use/` is retained for traceability only and is prohibited for analysis or report writing. Phase 4 working packages, duplicate or intermediate preregistrations, the failed original Phase 4A proposal and temporary release subsets are also non-authoritative and excluded from this release. See:

- `99_Superseded_File_List/SUPERSEDED_FILES.md`
- `99_Superseded_File_List/PHASE4_SUPERSEDED_AND_EXCLUDED.md`

## Audit records

Final audit records are in `05_Audit_Records/`, including the Phase 4A PASS decision, the complete Phase 4B computational audit and the final Phase 4 status record.
