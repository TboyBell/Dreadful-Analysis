# PHASE4_HANDOFF

**Project:** DAM140 Big Data Analytics and Visualization Assessment  
**Workspace/chat:** `01_Phase4_Builder`  
**Handoff date:** 30 July 2026  
**Document status:** Continuity and audit-gate record only  
**Modelling status:** **No models fitted; no performance results generated**  
**Frozen-input rule:** All completed Phase 1–3 files are read-only and must not be modified, renamed, overwritten, regenerated, or replaced.

---

## 1. Project context

This project analyses the Algerian Forest Fires dataset for the DAM140 final assessment. The assessment requires three research questions, data exploration and cleaning, justified analysis and evaluation techniques, a results summary, discussion of a scalable large-data architecture, three salient privacy issues, and Harvard-formatted references. Each substantive report section has a 300-word maximum, and no more than five diagrams or screenshots may appear in the report.

Phase 2 cleaning and Phase 3 exploratory analysis have passed independent audit and are frozen. Phase 4 is the modelling phase. New Phase 4 work must remain separate from the frozen release until it passes its own independent audit.

The Phase 4A modelling direction has been proposed, but the independent audit returned **FAIL — revise before implementation** because the plan was not yet fully pre-registered and contained two leakage risks. Therefore, **Phase 4B cannot start until a corrected Phase 4A plan passes independent audit**.

---

## 2. Continuity-verification table

| Filename | Purpose | Successfully accessed? | Authoritative and frozen? | Important information extracted |
|---|---|---:|---|---|
| `MASTER_MANIFEST.csv` | Master inventory, status, paths, sizes and SHA-256 hashes | Yes | Yes; package control record | Identifies authoritative Phase 1–3 files, frozen status, and superseded archive. Hashes were used to verify available files. |
| `RELEASE_NOTES.md` | Frozen release status and Phase 4 starting instructions | Yes | Yes; package control record | Phase 2 and Phase 3 passed independent audit; Phase 4 must start from the cleaned CSV and frozen Phase 3 summary; Figures B–D occupy three of five report slots; archived files must not be used. |
| `PHASE3_FROZEN_SUMMARY.md` (uploaded as `PHASE3~2.MD`) | Authoritative Phase 3 conclusions and research questions | Yes; SHA-256 matches manifest | Yes; Phase 3 frozen | Supplies target-provenance conclusion, final research questions, effect sizes, regional result, dry-run finding, repaired-record sensitivity and audit status. |
| `PHASE3_FROZEN_README.md` (uploaded as `PHASE3~1.MD`) | Phase 3 execution and figure documentation | Yes; SHA-256 matches manifest | Yes; Phase 3 frozen | Confirms 244×17 input, Phase 3 outputs, purposes of Figures B–D, and two remaining report figure slots. |
| `Algerian_forest_fires_dataset_CLEANED.csv` | Authoritative modelling dataset | Yes; SHA-256 matches manifest | Yes; Phase 2 frozen | 244 rows × 17 columns; 122 rows per region; 138 `fire`, 106 `not fire`; no missing values or duplicate region-date rows; one `record_repaired=True` row. |
| `phase3_frozen.py` | Authoritative reproducible Phase 3 analysis | Yes; SHA-256 matches manifest | Yes; Phase 3 frozen | Reproduces pooled/per-region comparisons, regional model specifications, temporal dependence, sensitivity checks, dry spells and Figures B–D. It explicitly preserves the target-provenance restriction. |
| `clean_forest_fires.py` | Authoritative Phase 2 cleaning pipeline | **No — not uploaded in this chat** | Yes per manifest; Phase 2 frozen | Manifest records its authoritative path and hash. It must not be reconstructed from memory or replaced by another script. |
| `Claude_Phase4A_Original.md.txt` | Original Phase 4A modelling and evaluation design | Yes | Working Phase 4 proposal; not an approved frozen phase | Provides the broad model direction: RQ1 baseline/logistic/tree/random forest, leave-one-month-out validation, RQ2 logistic specifications and descriptive RQ3. |
| `ChatGPT_Phase4A_Audit.md.txt` | Independent audit of the original Phase 4A design | Yes | Authoritative audit input for the current revision; Phase 4A itself has not passed | Accepts the broad direction but records ten blocking corrections and a final gate decision of FAIL. |
| `BDAV_Final_Assessment_Report__July_2026_docx-1.docx` (uploaded as `BDAV_F~1.DOC`) | Assessment brief and deliverables | Yes; SHA-256 matches manifest | Yes; assessment document frozen | Requires the Algerian dataset, three research questions, justified analysis, Harvard references, no more than five visuals, final CSV file(s), and completed Word/PDF report. |
| `DAM140_Final_Assignment_Answer_Template-1.docx` (uploaded as `DAM140~1.DOC`) | Mandatory report structure | Yes; SHA-256 matches manifest | Yes; assessment document frozen | Defines eight responses: five data-analysis sections, large-data architecture, privacy, and references; substantive responses are capped at 300 words; report must be anonymous. |
| `Grading_schema.pdf` (uploaded as `GRADIN~1.PDF`) | 28-point grading rubric | Yes; SHA-256 matches manifest | Yes; assessment document frozen | “Excellent” requires clear, well-justified research questions, evaluation, cleaning, techniques/criteria, results mapped to all questions, distributed/high-velocity architecture justification, and three privacy issues tied to relevant law and mitigation. |
| `BOOK_Chapter_Springer_ABID.pdf` | Original Abid and Izeboudjen (2020) research source | Yes; SHA-256 matches manifest | Yes; reference source frozen | Page 367 states that instances were first classified as `fire`/`not fire` using FWI and FFMC; the paper does not report the exact threshold rule. FFMC is calculated from Temperature, RH, wind and Rain. |
| Figures `fig_B_weather_by_class.png`, `fig_C_monthly_class_proportion.png`, `fig_D_fwi_weekly_trend.png` | Frozen Phase 3 report figures | **No — individual image files not uploaded in this chat** | Yes per manifest; Phase 3 frozen | Their purposes and frozen hashes are available through the manifest/README. They occupy three of the maximum five report visual slots. |
| `AUDIT_STATUS.md`, `PHASE2_AUDIT_DECISION.txt`, `PHASE3_AUDIT_DECISION.txt` | Frozen audit records | **No — not uploaded in this chat** | Yes per manifest | The release notes and frozen summaries confirm the resulting audit status; the records themselves must not be recreated. |
| `SUPERSEDED_FILES.md` and `99_Superseded_File_List/Archive_Do_Not_Use/` | Traceability and obsolete artefacts | **No — not uploaded in this chat** | The list is authoritative; archived contents are explicitly non-authoritative | Manifest and release notes are sufficient to enforce the prohibition: nothing in the archive may be used in Phase 4 or the report. |

### Verification note

Available frozen files with manifest entries were checked against their SHA-256 hashes. The cleaned CSV, Phase 3 script, Phase 3 summary/README, assessment brief, report template, rubric and Abid paper match the manifest. The Phase 4A plan and audit are later working documents and are not listed in the Phase 1–3 frozen manifest. `MASTER_MANIFEST.csv` and `RELEASE_NOTES.md` are package-level control files and are not self-listed in the manifest.

No unavailable file has been substituted, recreated, or inferred to be present.

---

## 3. Frozen Phase 2 and Phase 3 status

1. Phase 2 cleaning has passed independent audit and is frozen.
2. Phase 3 exploratory analysis has passed independent audit and is frozen.
3. The cleaned dataset is the sole authorised modelling dataset.
4. The Phase 3 research questions, provenance conclusion, calculations, wording and figure allocation must be preserved.
5. Frozen files may be read and referenced but may not be edited, renamed, overwritten, regenerated, replaced, or silently “improved.”
6. Any genuine dependency error discovered later must be escalated for audit; it does not authorise unilateral modification.
7. All Phase 4 working files must be created separately under `04_Phase_4_Modelling_Working/`.
8. Phase 4 outputs must not be added to the frozen package until Phase 4 passes independent audit.

---

## 4. Authoritative file list

### 4.1 Authoritative files available and verified in this chat

- `MASTER_MANIFEST.csv`
- `RELEASE_NOTES.md`
- `02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_README.md`
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`
- `03_Phase_3_EDA_Frozen/phase3_frozen.py`
- `00_Assessment_Documents/BDAV_Final_Assessment_Report__July_2026_docx-1.docx`
- `00_Assessment_Documents/DAM140_Final_Assignment_Answer_Template-1.docx`
- `00_Assessment_Documents/Grading_schema.pdf`
- `04_References/BOOK_Chapter_Springer_ABID.pdf`

### 4.2 Authoritative files listed in the manifest but not available in this chat

- `02_Phase_2_Cleaning_Frozen/clean_forest_fires.py`
- `02_Phase_2_Cleaning_Frozen/PHASE2_FROZEN_README.md`
- `02_Phase_2_Cleaning_Frozen/PHASE2_MANIFEST.csv`
- `03_Phase_3_EDA_Frozen/requirements.txt`
- `03_Phase_3_EDA_Frozen/fig_B_weather_by_class.png`
- `03_Phase_3_EDA_Frozen/fig_C_monthly_class_proportion.png`
- `03_Phase_3_EDA_Frozen/fig_D_fwi_weekly_trend.png`
- `05_Audit_Records/AUDIT_STATUS.md`
- `05_Audit_Records/PHASE2_AUDIT_DECISION.txt`
- `05_Audit_Records/PHASE3_AUDIT_DECISION.txt`
- `99_Superseded_File_List/SUPERSEDED_FILES.md`
- Phase 1 original-data files listed by the manifest

The manifest record may be used to identify these files and their status. Their contents must not be invented or reconstructed.

### 4.3 Phase 4 working inputs

- `Claude_Phase4A_Original.md.txt`
- `ChatGPT_Phase4A_Audit.md.txt`
- This handoff: `PHASE4_HANDOFF.md`

The original Phase 4A plan is a proposal, not an approved design. The audit is the controlling gate for its correction.

---

## 5. Files that must not be used

Nothing within `99_Superseded_File_List/Archive_Do_Not_Use/` may be used for modelling, figures, numerical results, or report text. The master manifest identifies the following archived examples:

- `chart1_class_balance.png`
- `chart2_correlation_heatmap.png`
- `chart3_weather_by_class.png`
- `chart4_fire_rate_region_month.png`
- `chart5_fwi_seasonal_trend.png`
- `chart6_multicollinearity_illustration.png`
- `eda_analysis.py`
- `fig_A_class_balance.png`
- `fig_C_fire_rate_region_month_CI.png`
- `fig_D_fwi_seasonal_trend_neutral.png`
- `fig_E_multicollinearity_by_region.png`
- `phase3_final.py`
- `phase3_revised_analysis.py`

Further prohibitions:

- Do not use an unverified copy of a frozen file.
- Do not substitute a superseded file for a missing authoritative file.
- Do not reconstruct missing frozen content from memory, chat history, or an obsolete script.
- Do not alter the cleaned CSV or create a “corrected” replacement without a separately audited dependency process.
- Do not overwrite or regenerate Figures B–D.
- Do not treat the failed original Phase 4A proposal as implementation authority.

---

## 6. Target-provenance conclusion

`Classes` is an **FWI/FFMC-derived class designation**.

It is **not independently observed wildfire incidence**, a confirmed wildfire event record, or ground-truth fire occurrence.

Abid and Izeboudjen state that the 244 instances were first classified as `fire` and `not fire` using the FWI system components FWI and FFMC. The exact thresholds or decision rule used to convert FWI and FFMC into the two classes are undocumented.

Consequences:

1. FWI and FFMC cannot be principal RQ1 predictors because they were used to construct the target.
2. DMC, DC, ISI and BUI also cannot be principal RQ1 predictors. They are FWI-system components or closely embedded computational quantities and would undermine the intended raw-weather reproduction question.
3. The permitted principal RQ1 predictors are Temperature, relative humidity, wind speed and Rain.
4. Even the raw-weather model is not independent validation: FFMC is calculated from those four weather inputs, so the model reproduces a designation generated from related quantities one computational step removed.
5. Performance must be described as **label-reproduction**, **class-designation reproduction**, or **out-of-month label-reproduction performance**.
6. It must not be described as validated wildfire prediction, real-fire detection, future-fire forecasting, or evidence that actual fires were correctly identified.
7. A false negative means failure to reproduce a recorded `fire` designation, not a missed real wildfire.

---

## 7. Final frozen research questions

1. **How accurately can Temperature, relative humidity, wind speed and rainfall reproduce the dataset’s FWI/FFMC-derived class designation, and which of these meteorological variables contribute most to that classification?**

2. **Does the association between region and the recorded FWI/FFMC-derived class designation persist after adjustment for the measured meteorological variables?**

3. **How do FWI values and the proportion of observations assigned the fire class vary across Bejaia and Sidi-Bel Abbes during June–September 2012?**

These questions are frozen and may not be rewritten in Phase 4 unless a genuine audited dependency error is established.

---

## 8. Verified Phase 3 findings relevant to modelling

### Dataset and class composition

- 244 complete records and 17 columns.
- 122 records for Bejaia and 122 for Sidi-Bel Abbes.
- 138 `fire` and 106 `not fire` designations.
- One record is flagged `record_repaired=True`.
- The repaired-record sensitivity analysis found no material change to conclusions.

### Weather/class comparisons

Authoritative pooled Cliff’s delta values:

- Temperature: `δ = 0.607` — large.
- Relative humidity: `δ = −0.494` — large when pooled.
- Wind speed: `δ = −0.023` — negligible.
- Rain: `δ = −0.725` — large.

The statistical-significance pattern occurred within both regions, but Bejaia’s relative-humidity effect was medium (`δ = −0.451`) rather than large. Numerical effect sizes are primary; qualitative magnitude labels are secondary.

### Region and specification sensitivity

- Unadjusted region–class association: `χ² = 6.02`, `p = 0.014`, Cramér’s `V = 0.157`.
- This is a small association in the June–September 2012 sample and is not causal evidence.
- The adjusted region coefficient changed materially across three logistic specifications.
- No single adjusted estimate is authoritative or definitive.

### Temporal dependence

Adjacent daily observations within each region are temporally dependent. Phase 3 found substantial autocorrelation in variables including Temperature, DC and FFMC. Standard independent-sample statistics were retained as descriptive summaries of this specific sample, not population inference.

This dependence is the reason ordinary random row-level cross-validation is not the primary Phase 4 validation design.

### Seasonal/dry-spell findings

A zero-rain run began before and continued through the late-August FWI peak week in both regions. Comparable dry runs elsewhere did not produce a comparable peak, so zero rainfall alone does not explain the peak timing.

### Figure allocation

Frozen Figures B, C and D occupy three of the maximum five report visual slots. Only two slots remain for Phase 4 outputs.

---

## 9. Accepted Phase 4A direction

The broad direction is accepted, subject to all audit corrections below:

### RQ1

- Compare a fold-trained majority baseline, fixed logistic regression, one fixed shallow decision tree and one fixed random forest.
- Use only Temperature, RH, wind speed and Rain as principal predictors.
- Use leave-one-month-out validation as the primary design.
- Keep same-date regional observations in the same held-out month.
- Describe the estimand as out-of-month reproduction of the class designation.
- Use balanced accuracy as the primary performance metric.
- Use raw Rain in the primary logistic model and `Rain > 0` only as a pre-registered sensitivity specification.
- Use fixed conservative parameters rather than hyperparameter tuning.
- Use standardised logistic coefficients and held-out random-forest permutation importance for distinct, clearly labelled feature-contribution questions.

### RQ2

- Continue the Phase 3 logistic specification-sensitivity approach.
- Fit the predeclared specifications on the full dataset for association analysis.
- Report the region coefficient, odds ratio, model-based 95% interval and AIC for each.
- Treat `Region × Rain` only as an exploratory sensitivity analysis and centre continuous variables before the interaction.
- Do not apply leave-one-month-out validation to answer RQ2.
- Do not use four-month cluster-robust standard errors.
- Do not make causal or “no association” claims.

### RQ3

- No new model is required.
- Frozen Figures C and D already answer the descriptive question.
- Any modelling added to RQ3 would be unnecessary complexity.

### Gate status

The broad direction is **not implementation permission**. The original Phase 4A plan failed audit. **Phase 4B cannot start until a corrected, exact and leakage-safe Phase 4A plan receives an independent PASS.**

---

## 10. Ten Phase 4A audit blockers/corrections

The revised Phase 4A design must implement all ten corrections:

1. **Determine the majority baseline inside each training fold.**  
   The constant class must be learned only from the current outer training data, then applied to the held-out month.

2. **Use raw Rain as primary and `Rain > 0` as sensitivity only.**  
   Do not use full-data AIC or held-out outcomes to choose a preferred Rain representation.

3. **Freeze exact model parameters, seeds and threshold.**  
   Every logistic, tree and random-forest setting, preprocessing rule, class-weight rule, random seed and classification threshold must be specified before fitting.

4. **Remove the random-CV inflation demonstration.**  
   Do not conduct a random five-fold comparison with a pre-assumed conclusion.

5. **Finalise metrics and aggregation.**  
   Define balanced accuracy as primary; define average precision rather than ambiguous PR-AUC; fix threshold at the approved value; report per-fold metrics, arithmetic mean and standard deviation, and separately labelled pooled out-of-fold metrics.

6. **Remove calibration curves and post-hoc partial dependence.**  
   These open-ended branches are not part of the core pre-registered plan.

7. **Simplify RQ2 and separate inference from predictive validation.**  
   Use a full-data specification table for RQ2, reserve the interaction for exploratory sensitivity, remove RQ2 LOMO validation and remove four-cluster robust standard errors.

8. **Specify logistic and permutation-importance procedures.**  
   Define the final post-validation logistic refit, standardisation and interpretation; calculate random-forest permutation importance on each held-out month using a fixed score, fixed repetitions, fixed seeds and a predeclared aggregation method.

9. **Define the preferred-model tie rule and failure handling.**  
   State exactly how ties are resolved and how convergence failures, undefined metrics, warnings or failed folds will be recorded without changing the plan after results are seen.

10. **Save fold assignments, out-of-fold predictions, metrics and settings.**  
    Preserve all reproducibility artefacts, including package versions, exact parameters and seeds.

A corrected Phase 4A document must make every item operational rather than leaving examples, ranges, “optional” branches, or decisions to be made after observing results.

---

## 11. Modelling and interpretation restrictions

### Input and leakage restrictions

- Use only the frozen cleaned CSV as the modelling dataset.
- Do not use FWI, FFMC, DMC, DC, ISI or BUI as principal RQ1 predictors.
- Do not include `Classes`, a recoded form of it, or an outcome-derived variable among predictors.
- Do not select the baseline class from the full dataset.
- Fit all learned preprocessing inside each outer training fold.
- Do not use held-out outcomes to select representations, hyperparameters, thresholds or features.
- Do not perform unregistered tuning.
- Do not optimise the classification threshold on pooled out-of-fold predictions.
- Do not add post-hoc analyses because a pattern “looks interesting” unless a new audited sensitivity plan is approved.

### Interpretation restrictions

- Use “designation,” “recorded class,” and “label reproduction.”
- Do not call `Classes` independently observed wildfire incidence.
- Do not call RQ1 a validated wildfire-prediction system.
- Do not interpret model importance as physical causation.
- Do not interpret region coefficients causally.
- Do not claim a non-significant result proves no regional association.
- Label RQ2 intervals as ordinary model-based intervals that may be optimistic because temporal dependence is not modelled.
- Keep conclusions bounded to two regions and one June–September 2012 season.

### Reporting restrictions

- Preserve the final research questions exactly.
- Preserve the frozen Phase 3 findings and authoritative effect-size wording.
- Do not change Figures B–D.
- Respect the five-visual maximum; only two Phase 4 visual slots remain.
- Keep technical supporting outputs outside the 300-word report sections when necessary.
- Maintain report anonymity.
- Use Harvard-formatted references.

---

## 12. Builder–auditor workflow

### Stage A — Builder revises Phase 4A

The builder creates an exact, leakage-safe pre-registration in `04_Phase_4_Modelling_Working/`. It must specify:

- exact outer-fold definitions;
- exact predictor sets and Rain sensitivity;
- exact pipelines;
- exact model parameters;
- exact random seeds;
- exact 0/1 label mapping and positive class;
- exact probability threshold;
- exact metrics and aggregation;
- exact model-selection/tie rule;
- exact failure handling;
- exact RQ2 specifications;
- exact feature-contribution procedures;
- exact planned outputs and filenames;
- exact two-figure plan;
- package/version capture.

No model may be fitted during this stage.

### Stage B — Independent Phase 4A audit

The auditor checks the revised plan against:

- frozen provenance and research questions;
- data leakage;
- temporal validation;
- exact reproducibility;
- assessment constraints;
- interpretation language;
- all ten blocking corrections.

The auditor returns PASS or FAIL with reasons.

### Stage C — Gate

- **FAIL:** revise the design; do not fit models.
- **PASS:** Phase 4B implementation becomes permitted.

### Stage D — Builder implements Phase 4B

The builder implements exactly the audited plan, without changing parameters or adding analyses after seeing results. All files remain in `04_Phase_4_Modelling_Working/`.

### Stage E — Independent Phase 4B audit

The auditor verifies code, inputs, folds, outputs, calculations, figures, wording, checksums and compliance with the passed Phase 4A plan.

### Stage F — Freeze

Only after Phase 4B passes audit may Phase 4 materials be frozen, added to a release package, and used as the authoritative basis for final report writing.

---

## 13. Required Phase 4B outputs

The corrected Phase 4A plan must freeze exact filenames. At minimum, Phase 4B must create code-generated, auditable equivalents of the following within `04_Phase_4_Modelling_Working/`:

### Code and configuration

- `phase4b_modelling.py` — single reproducible implementation entry point.
- `PHASE4B_MODEL_SPECIFICATION.json` — exact predictors, parameters, seeds, thresholds, metrics, tie rule and failure rules.
- `PHASE4B_REQUIREMENTS.txt` or environment export — exact package versions.
- `PHASE4B_RUN_LOG.txt` — execution log, warnings and failure status.

### Validation and predictions

- `fold_assignments.csv` — immutable row/date/month assignments and any boundary-gap sensitivity exclusions.
- `oof_predictions.csv` — true class, fold, model, predicted class and predicted probability where applicable.
- `fold_metrics.csv` — per-model, per-held-out-month metrics.
- `metric_summary.csv` — arithmetic mean and standard deviation across folds.
- `pooled_oof_metrics.csv` — separately labelled pooled out-of-fold metrics.
- `pooled_confusion_matrices.csv` — code-generated confusion matrices.
- Baseline predictions must be present in the same auditable outputs and must be trained fold by fold.

### Feature contribution

- `logistic_full_data_coefficients.csv` — post-validation full-data refit using the unchanged audited primary specification, with standardised coefficients/odds ratios and model-based intervals.
- `permutation_importance_by_fold.csv` — held-out-month permutation results using the predeclared score, repetitions and seeds.
- `permutation_importance_summary.csv` — predeclared aggregation across folds.

### RQ2

- `rq2_specification_results.csv` — region coefficient, odds ratio, model-based interval, AIC and convergence status for each predeclared specification.
- `rq2_interaction_sensitivity.csv` — exploratory centred `Region × Rain` comparison, kept separate from the primary specifications.

### Sensitivity analyses

- `rain_binary_sensitivity_metrics.csv` — pre-registered `Rain > 0` logistic sensitivity, not a replacement for the primary raw-Rain model.
- `boundary_gap_sensitivity_metrics.csv` — only if retained and approved in revised Phase 4A.

### Figures

Two code-generated report candidates, subject to the passed Phase 4A decision:

1. Fold-level balanced accuracy by held-out month and model, including the fold-trained baseline.
2. Standardised logistic coefficient/odds-ratio plot, with intervals labelled model-based and not adjusted for temporal dependence.

A confusion matrix remains a table, not a figure.

### Integrity and documentation

- `PHASE4B_README.md` — execution, inputs, outputs and interpretation limits.
- `PHASE4B_MANIFEST.csv` — filename, purpose, status, size and SHA-256 for every Phase 4B artefact.
- A machine-readable copy of all exact settings.
- No manual edits to numerical tables or figures after generation.

The exact names may be refined only in the revised Phase 4A plan before audit; the output categories and reproducibility content are mandatory.

---

## 14. Limitations to carry into Phase 4 and the report

1. `Classes` is derived from FWI/FFMC rather than independent fire observations.
2. The class-construction thresholds are undocumented.
3. Raw weather inputs are computationally related to FFMC, so RQ1 remains label reproduction rather than external validation.
4. The dataset is small: 244 observations.
5. It covers only two Algerian regions.
6. It covers only one four-month season in 2012.
7. Daily observations are temporally dependent.
8. Leave-one-month-out has only four outer folds; fold metrics will be variable.
9. Class prevalence changes substantially across months.
10. Same-day regional observations are not independent replicas of different dates.
11. Ordinary logistic intervals do not account fully for temporal dependence and may overstate precision.
12. Correlated predictors can destabilise logistic coefficients and divide random-forest permutation importance.
13. Feature importance is model-dependent and is not causal evidence.
14. The adjusted region estimate is known to be specification-dependent.
15. The one repaired record is retained and flagged; Phase 3 found no material sensitivity to it.
16. Three report figure slots are already consumed, leaving only two for Phase 4.
17. Report word limits require technical detail to be preserved in reproducibility files rather than crowded into the final narrative.

---

## 15. Next permitted action

The next permitted action is:

> **Create a corrected Phase 4A pre-registration that implements all ten audit corrections, freezes every model/evaluation choice, and submit that design for independent audit.**

Before Phase 4B, the builder must also preserve the manifest record that `clean_forest_fires.py` and several other frozen artefacts are unavailable in this chat; no substitute may be used. Their absence does not authorise alteration of the hash-verified cleaned CSV.

**Phase 4B model fitting, performance calculation, feature-importance calculation and figure generation are not permitted until the revised Phase 4A design receives an explicit independent PASS.**

---

## 16. Handoff status

- Continuity from frozen Phase 2 and Phase 3: preserved.
- Available authoritative files: inspected.
- Available manifest-listed files: hash-verified.
- Missing authoritative files: identified explicitly.
- Superseded files: prohibited.
- Target provenance: preserved.
- Research questions: preserved.
- Phase 3 findings: preserved.
- Phase 4A broad direction: recorded.
- Ten audit blockers: recorded.
- Model fitting: not performed.
- Performance results: not generated.
- Frozen files: not modified.

**Handoff complete. Audit gate remains closed.**
