# PHASE4A_REVISED_PREREGISTRATION

**Project:** DAM140 Big Data Analytics and Visualization Assessment  
**Workspace/chat:** `01_Phase4_Builder`  
**Document role:** Corrected Phase 4A modelling and evaluation pre-registration  
**Controlling document:** `PHASE4_HANDOFF.md`  
**Audit basis:** `ChatGPT_Phase4A_Audit.md.txt`  
**Status:** **Ready for independent Phase 4A audit; implementation not authorised**  
**Audit gate:** **Closed until `02_Phase4_Auditor` gives an explicit PASS**  
**Frozen-input rule:** Every completed Phase 1–3 file remains read-only and must not be modified, renamed, overwritten, regenerated, or replaced.  
**Current analytical status:** No model has been fitted, no performance metric has been calculated, and no figure has been generated.

**Canonical authority:** `PHASE4A_REVISED_PREREGISTRATION.md` is the sole canonical Phase 4A implementation authority submitted for final PASS.

**Supersession control:** The earlier pre-correction preregistration is superseded, is retained for audit history only, and is not authorised for Phase 4B. It must not be included among the authoritative Phase 4B implementation inputs.

## Narrow correction table

| Auditor issue | Exact correction | Sections changed |
|---|---|---|
| Circular dependency between `PHASE4B_MANIFEST.csv` and `PHASE4B_RUN_LOG.txt` | The manifest excludes both itself and the run log. The manifest is finalised and hashed first; its filename, hash, final status and completion timestamp are then appended to the run log, which is intentionally the final file written. | Sections 24 and 26 |
| Pre-interpreter environment controls | `PYTHONHASHSEED`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS` and `NUMEXPR_NUM_THREADS` must be established in the process or shell environment before Python starts. The script records observed values and does not claim that setting them after startup is retroactive. | Section 25 |
| Baseline tie-rule implementation clarity | Baseline class predictions are generated directly from training counts and the fixed tie rule. The stored training-prevalence probability is a separate audit field and is never thresholded to produce the baseline class. | Section 9 |

---

## 1. Authority, scope and provenance

This canonical pre-registration implements the next permitted action in `PHASE4_HANDOFF.md`. The handoff and the independent audit override the failed original Phase 4A proposal wherever they conflict. Only `PHASE4A_REVISED_PREREGISTRATION.md` may be used as the Phase 4B implementation authority; earlier working or pre-correction versions are audit-history records only.

The authoritative analytical input is:

`02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`

The locally available copy has 244 rows and 17 columns and has SHA-256:

`9b24dd2ee6e5678ebb323ceb9b9e8d8f1d351df3974b80ca2ebf49d69a73da6a`

The authoritative frozen Phase 3 summary has SHA-256:

`106f6f368bba10521329c1bfbb43e4abcf71ebb81abf8ca1e9f31d7cba933a14`

The authoritative frozen Phase 3 script has SHA-256:

`b5c1defcc4b333ad32b8e626eb3e78003a49e46ae8811f98ab017b4d7f9aae57`

At the start of Phase 4B, these hashes must be recomputed and compared with `MASTER_MANIFEST.csv`. A mismatch closes the implementation run immediately.

### Target provenance

`Classes` is an **FWI/FFMC-derived designation**. It is not independently observed wildfire incidence, confirmed fire occurrence, or external ground truth. Abid and Izeboudjen state that the observations were first assigned to `fire` and `not fire` using FWI and FFMC. The exact thresholds or decision rule are undocumented.

The principal RQ1 predictor set is therefore restricted to:

- `Temperature`
- `RH`
- `Ws`
- `Rain`

The following variables are prohibited as principal RQ1 predictors:

- `FWI`
- `FFMC`
- `DMC`
- `DC`
- `ISI`
- `BUI`

Even the permitted raw-weather model is not independent wildfire validation because FFMC is calculated from Temperature, relative humidity, wind speed and Rain. Every RQ1 result must be described as reproduction of the recorded class designation, not validated wildfire prediction.

---

## 2. Frozen research questions

### RQ1

**How accurately can Temperature, relative humidity, wind speed and rainfall reproduce the dataset’s FWI/FFMC-derived class designation, and which of these meteorological variables contribute most to that classification?**

### RQ2

**Does the association between region and the recorded FWI/FFMC-derived class designation persist after adjustment for the measured meteorological variables?**

### RQ3

**How do FWI values and the proportion of observations assigned the fire class vary across Bejaia and Sidi-Bel Abbes during June–September 2012?**

The wording of these three questions is frozen.

---

## 3. Audit-resolution table

| Audit blocker | Operational resolution in this pre-registration | Phase 4B compliance evidence |
|---|---|---|
| 1. Full-data majority baseline | The majority class is determined independently inside each outer training fold. A tie is resolved as `not fire`. | `baseline_training_counts.csv`, `fold_assignments.csv`, `oof_predictions.csv` |
| 2. Rain representation leakage | Raw `Rain` in millimetres is the sole primary representation. `Rain_any = 1[Rain > 0]` replaces raw Rain only in one fixed logistic sensitivity analysis. It cannot replace the primary model. | `PHASE4B_MODEL_SPECIFICATION.json`, `rain_binary_sensitivity_metrics.csv` |
| 3. Unfrozen parameters, seeds and threshold | Every estimator, preprocessing step, seed and threshold is fixed in Sections 9–13. No hyperparameter search is authorised. | Model specification JSON, run log, environment record |
| 4. Random-CV inflation demonstration | No random split, random k-fold, stratified random CV, repeated random CV or comparison intended to demonstrate inflation will be run. | Absence from code and output manifest; auditor code review |
| 5. Metrics and aggregation incomplete | Metrics, class conventions, threshold, per-fold calculation, unweighted mean, sample SD and pooled out-of-fold rules are fixed in Sections 14–15. | `fold_metrics.csv`, `metric_summary.csv`, `pooled_oof_metrics.csv` |
| 6. Open calibration and partial-dependence branches | Calibration curves, calibration fitting, Brier score, partial-dependence plots and post-hoc nonlinear exploration are excluded. | Absence from code and output manifest |
| 7. RQ2 mixed inference and prediction | RQ2 uses full-data logistic specification analysis only. LOMO is not used for RQ2. Four-cluster robust standard errors are excluded. | `rq2_specification_results.csv`, `rq2_interaction_sensitivity.csv` |
| 8. Feature-contribution procedures incomplete | The post-validation logistic refit and held-out random-forest permutation procedure are fully fixed in Sections 18–19. | Coefficient and permutation-importance outputs |
| 9. Tie and failure handling undefined | Eligibility, model preference, practical ties, warning capture, undefined metrics and failed folds are fixed in Sections 16–17. | `warnings_and_failures.csv`, model-selection fields in summary |
| 10. Reproducibility artefacts incomplete | Fold assignments, predictions, metrics, settings, package versions, input hashes, run log and output hashes are mandatory. | Exact output manifest in Section 24 |

---

## 4. Final technique mapping

| Research question | Analytical role | Fixed technique | Evaluation or reporting basis | Explicit exclusion |
|---|---|---|---|---|
| RQ1 | Classification and feature contribution | Fold-trained majority baseline; unpenalised logistic regression; one shallow decision tree; one random forest | Four-fold leave-one-month-out label-reproduction performance; balanced accuracy primary; standardised logistic odds ratios; held-out RF permutation importance | FWI-system predictors, random CV, tuning, calibration, partial dependence |
| RQ2 | Association and specification sensitivity | Four full-data binomial-logit specifications, with the fourth held separately as an exploratory `Region × Rain` sensitivity | Region coefficient, odds ratio, ordinary model-based 95% CI and AIC; one planned likelihood-ratio test comparing models R2 and R3 | LOMO, predictive model selection, cluster-robust SEs, causal interpretation |
| RQ3 | Descriptive seasonal comparison | Frozen Phase 3 Figures C and D and frozen Phase 3 numerical findings | Descriptive interpretation only | Forecasting, new time-series modelling, new Phase 4 calculations |

---

## 5. RQ1 target, labels and predictors

### 5.1 Target mapping

The fixed binary mapping is:

- `not fire` → `0`
- `fire` → `1`

The positive class is `fire` (`1`).

No other spelling, whitespace variant or class value is accepted. Unexpected labels cause an input-validation failure.

### 5.2 Probability threshold

For logistic regression, decision tree and random forest:

- predicted `fire` when `P(fire) >= 0.500000`
- predicted `not fire` when `P(fire) < 0.500000`

The threshold is not tuned, moved, calibrated or selected from out-of-fold results.

### 5.3 Primary predictor definitions

The predictor order is frozen as:

1. `Temperature` — numeric Celsius value from the cleaned CSV.
2. `RH` — numeric relative humidity percentage from the cleaned CSV.
3. `Ws` — numeric wind speed in km/h from the cleaned CSV.
4. `Rain` — numeric rainfall value in millimetres from the cleaned CSV.

No date, day, month, year, region, repaired-record flag or FWI-system variable is included in RQ1 predictors.

### 5.4 Rain sensitivity definition

One deterministic sensitivity variable is authorised:

`Rain_any = 1` when `Rain > 0.0`, otherwise `Rain_any = 0`.

The fixed sensitivity predictor order is:

1. `Temperature`
2. `RH`
3. `Ws`
4. `Rain_any`

This sensitivity is fitted only with the same unpenalised logistic model. It is excluded from model preference, permutation importance, the two report figures and any replacement of the raw-Rain primary specification.

---

## 6. Input validation and immutable row identifier

Phase 4B must read the frozen CSV without rewriting it.

A one-based immutable identifier named `source_row_id` is assigned from the physical CSV data-row order after the header:

- first data row → `source_row_id = 1`
- final data row → `source_row_id = 244`

Before any estimator is created, Phase 4B must verify:

- exact row count: `244`
- exact column count: `17`
- exact required columns and spellings:
  `day`, `month`, `year`, `Temperature`, `RH`, `Ws`, `Rain`, `FFMC`, `DMC`, `DC`, `ISI`, `BUI`, `FWI`, `Classes`, `Region`, `record_repaired`, `date`
- no missing values in required modelling or fold columns
- months exactly `{6, 7, 8, 9}`
- year exactly `{2012}`
- regions exactly `{Bejaia, Sidi-Bel Abbes}`
- classes exactly `{not fire, fire}`
- no duplicate `(Region, date)` pair
- each date belongs to its recorded numeric month and year
- each modelling predictor is finite and numeric
- input SHA-256 equals the manifest value

Failure of any check terminates Phase 4B before fitting and records the reason in `PHASE4B_RUN_LOG.txt` and `warnings_and_failures.csv`. The input file is never repaired during Phase 4.

---

## 7. Exact primary leave-one-month-out design

The primary validation design contains exactly four non-random outer folds.

| Fold ID | Held-out month | Test dates | Training months | Test inclusion |
|---|---:|---|---|---|
| `F06` | June (`6`) | 2012-06-01 through 2012-06-30 | July, August, September | Every June row from both regions |
| `F07` | July (`7`) | 2012-07-01 through 2012-07-31 | June, August, September | Every July row from both regions |
| `F08` | August (`8`) | 2012-08-01 through 2012-08-31 | June, July, September | Every August row from both regions |
| `F09` | September (`9`) | 2012-09-01 through 2012-09-30 | June, July, August | Every September row from both regions |

Rules:

1. No rows are shuffled.
2. The complete held-out month is used only for testing in its fold.
3. Both regional observations for the same date remain in the same fold.
4. Primary training uses every row outside the held-out month.
5. Each source row receives an out-of-fold prediction exactly once for each primary model.
6. Training on months after the held-out block is accepted because RQ1 estimates retrospective out-of-month designation reproduction, not prospective forecasting.
7. No random validation comparison is run.

`fold_assignments.csv` uses long format with one row for every `source_row_id × fold_id` combination and contains:

- `source_row_id`
- `date`
- `Region`
- `Classes`
- `fold_id`
- `held_out_month`
- `primary_role` with values `train` or `test`
- `gap_role` with values `train`, `test` or `excluded_gap`

---

## 8. Exact three-day boundary-gap sensitivity

The boundary-gap sensitivity uses the same held-out test month as the primary design. It removes from training both regional observations for each available date within three calendar days immediately before the test-month start and three calendar days immediately after the test-month end.

The exact exclusions are:

| Fold | Training dates excluded from the gap sensitivity |
|---|---|
| `F06` | 2012-07-01, 2012-07-02, 2012-07-03 |
| `F07` | 2012-06-28, 2012-06-29, 2012-06-30, 2012-08-01, 2012-08-02, 2012-08-03 |
| `F08` | 2012-07-29, 2012-07-30, 2012-07-31, 2012-09-01, 2012-09-02, 2012-09-03 |
| `F09` | 2012-08-29, 2012-08-30, 2012-08-31 |

The gap sensitivity reruns only:

- fold-trained majority baseline
- primary raw-Rain logistic regression
- decision tree
- random forest

It uses the same parameters, threshold, preprocessing and held-out rows as the primary analysis.

The gap sensitivity:

- does not include the `Rain_any` logistic sensitivity;
- does not generate permutation importance;
- does not determine the preferred model;
- does not change the primary results;
- is reported separately as a robustness check.

---

## 9. Exact fold-trained majority baseline

For each fold and each analysis variant:

1. Count `fire` and `not fire` in that fold’s permitted training rows.
2. Generate the baseline class directly from the training counts:
   - when `training_fire_count > training_not_fire_count`, select `fire`;
   - when `training_fire_count < training_not_fire_count`, select `not fire`;
   - when the counts are equal, select `not fire`.
3. Assign the selected majority class to every held-out row. The baseline class is generated only by the count comparison and tie rule; it is never generated by thresholding a probability field.
4. Separately calculate and save the audit score `training_fire_count / training_row_count` as `predicted_probability_fire`. This stored training-prevalence probability does not determine the baseline class and therefore cannot override the theoretical tie rule.
5. Save:
   - training fire count;
   - training not-fire count;
   - selected majority class;
   - training fire prevalence;
   - held-out predicted class;
   - stored training-prevalence probability.
6. Compute threshold-based metrics from the directly generated baseline class only:
   - accuracy;
   - balanced accuracy;
   - fire precision;
   - fire recall;
   - fire F1;
   - confusion matrix.
7. Set baseline ROC-AUC and baseline average precision to `NA_NOT_APPLICABLE_CONSTANT_BASELINE`.
8. Use the diagonal line as the ROC no-skill reference and held-out positive prevalence as the average-precision no-skill reference in technical interpretation; no ROC figure is allocated.

The descriptive full-dataset class balance must not define the baseline.

---

## 10. Leakage-safe preprocessing

### 10.1 General rules

- No imputation is performed because missing values are prohibited by input validation.
- No feature selection is performed.
- No learned transformation uses held-out data.
- No hyperparameter tuning is performed.
- No probability calibration is performed.
- No threshold selection is performed.
- No outcome-derived preprocessing is performed.

### 10.2 Primary logistic preprocessing

For each outer training fold:

1. Select primary predictors in the fixed order:
   `Temperature`, `RH`, `Ws`, `Rain`.
2. Fit `sklearn.preprocessing.StandardScaler` on training predictors only with:
   - `with_mean=True`
   - `with_std=True`
   - variance divisor `n` (`ddof=0`, the StandardScaler definition)
   - `copy=True`
3. Transform the training predictors using the training means and standard deviations.
4. Transform held-out predictors using the unchanged training-fold scaler.
5. Add an intercept column of ones after scaling.
6. Fit the fixed statsmodels binomial-logit model in Section 11.
7. Save each fold’s means, scales and feature order.

A zero training-fold scale for any predictor is a failed logistic fold. The predictor is not removed and the scale is not replaced.

### 10.3 Rain-any logistic sensitivity preprocessing

For each outer training fold:

1. Fit StandardScaler on `Temperature`, `RH` and `Ws` using training data only.
2. Pass `Rain_any` unchanged as `0` or `1`.
3. Arrange transformed columns as:
   `Temperature_z`, `RH_z`, `Ws_z`, `Rain_any`.
4. Add an intercept.
5. Fit the same fixed statsmodels binomial-logit model.

### 10.4 Decision-tree preprocessing

Use the raw primary predictors in the frozen order. No centring, scaling, binning or transformation is applied.

### 10.5 Random-forest preprocessing

Use the raw primary predictors in the frozen order. No centring, scaling, binning or transformation is applied.

---

## 11. Exact RQ1 logistic-regression specification

The primary and Rain-any sensitivity logistic models use:

- implementation: `statsmodels.api.GLM`
- response family: `statsmodels.families.Binomial`
- link: logit
- intercept: included
- penalty: none
- regularisation strength: none
- class weights: none
- frequency weights: none
- variance weights: none
- offset: none
- exposure: none
- fitting method: iteratively reweighted least squares (`IRLS`)
- starting parameters: statsmodels default
- maximum iterations: `200`
- convergence tolerance: `1e-8`
- covariance type for final full-data coefficient output: `nonrobust`
- probability threshold: `0.500000`
- random seed: no stochastic operation is used by GLM; global seed controls the run environment
- positive class: `fire`
- predictor order: fixed by Section 5
- preprocessing: fixed by Section 10

Convergence is accepted only when the fitted result reports convergence and every coefficient, standard error and predicted probability required for that stage is finite.

No alternative solver, penalised fallback, variable removal or coefficient clipping is authorised.

---

## 12. Exact decision-tree specification

Use `sklearn.tree.DecisionTreeClassifier` with:

- `criterion="gini"`
- `splitter="best"`
- `max_depth=3`
- `min_samples_split=20`
- `min_samples_leaf=10`
- `min_weight_fraction_leaf=0.0`
- `max_features=None`
- `random_state=140`
- `max_leaf_nodes=None`
- `min_impurity_decrease=0.0`
- `class_weight=None`
- `ccp_alpha=0.0`
- `monotonic_cst=None`

Additional fixed rules:

- raw primary predictors only;
- no pruning after fitting;
- no class reweighting;
- no resampling;
- probability threshold `0.500000`;
- `predict_proba` column is located using `estimator.classes_` and the encoded positive class `1`.

---

## 13. Exact random-forest specification

Use `sklearn.ensemble.RandomForestClassifier` with:

- `n_estimators=500`
- `criterion="gini"`
- `max_depth=4`
- `min_samples_split=10`
- `min_samples_leaf=5`
- `min_weight_fraction_leaf=0.0`
- `max_features="sqrt"`
- `max_leaf_nodes=None`
- `min_impurity_decrease=0.0`
- `bootstrap=True`
- `oob_score=False`
- `n_jobs=1`
- `random_state=140`
- `verbose=0`
- `warm_start=False`
- `class_weight=None`
- `ccp_alpha=0.0`
- `max_samples=None`
- `monotonic_cst=None`

Additional fixed rules:

- raw primary predictors only;
- no class reweighting;
- no resampling outside the estimator’s fixed bootstrap procedure;
- no OOB metric;
- probability threshold `0.500000`;
- `predict_proba` column is located using `estimator.classes_` and encoded positive class `1`.

---

## 14. Final RQ1 metric definitions

The primary metric is **balanced accuracy**.

For held-out predictions:

- `TP`: true `fire`, predicted `fire`
- `TN`: true `not fire`, predicted `not fire`
- `FP`: true `not fire`, predicted `fire`
- `FN`: true `fire`, predicted `not fire`

Metrics:

1. **Accuracy**  
   `(TP + TN) / (TP + TN + FP + FN)`

2. **Fire recall / sensitivity**  
   `TP / (TP + FN)`

3. **Not-fire recall / specificity**  
   `TN / (TN + FP)`

4. **Balanced accuracy — primary**  
   `(fire recall + not-fire recall) / 2`

5. **Fire precision**  
   `TP / (TP + FP)`

6. **Fire F1**  
   `2 × precision × recall / (precision + recall)`

7. **ROC-AUC**  
   Area under the ROC curve calculated from unthresholded `P(fire)` for logistic regression, decision tree and random forest.

8. **Average precision**  
   Non-interpolated average precision calculated from unthresholded `P(fire)`. The term `PR-AUC` is not used.

9. **Confusion matrix**  
   Fixed row order: actual `not fire`, actual `fire`.  
   Fixed column order: predicted `not fire`, predicted `fire`.

Metric implementation uses scikit-learn with:

- `balanced_accuracy_score`
- `accuracy_score`
- `precision_score(pos_label=1, zero_division=0)`
- `recall_score(pos_label=1, zero_division=0)`
- `f1_score(pos_label=1, zero_division=0)`
- `roc_auc_score`
- `average_precision_score`
- `confusion_matrix(labels=[0, 1])`

No calibration metric is calculated.

---

## 15. Metric aggregation and reporting

### 15.1 Per-fold results

Every authorised model/variant receives one metric row for each held-out month.

The primary model comparison uses only:

- fold-trained majority baseline;
- primary raw-Rain logistic regression;
- decision tree;
- random forest.

The Rain-any sensitivity and boundary-gap sensitivity remain separately labelled.

### 15.2 Across-fold summary

For each metric and model:

- arithmetic mean across the four folds;
- sample standard deviation across the four folds using `ddof=1`;
- fold count.

No fold weighting is used in the mean or SD.

A mean and SD are produced only when all four required fold values are finite. Otherwise, both are recorded as missing and the failure reason is attached.

### 15.3 Pooled out-of-fold results

For each model/variant, concatenate the held-out predictions so that each source row appears exactly once. Compute pooled metrics on the concatenated rows.

Pooled metrics are labelled `pooled_oof` and are not described as the same quantity as the unweighted fold mean.

### 15.4 Rounding

- All computations and model-selection rules use unrounded floating-point values.
- CSV outputs retain at least 15 significant decimal digits where supported.
- Display tables use three decimal places.
- P-values use four significant digits, with values below `0.0001` displayed as `<0.0001`.
- Rounding never determines a model decision.

---

## 16. Preferred-model rule and tie breaking

Only these three primary candidate models are eligible:

1. primary raw-Rain logistic regression;
2. decision tree;
3. random forest.

The majority baseline is a benchmark, not a candidate. The Rain-any logistic sensitivity and boundary-gap sensitivity are excluded from model preference.

### 16.1 Eligibility

A candidate is eligible only when:

- all four primary folds fitted successfully;
- all four primary-fold balanced-accuracy values are finite;
- all 244 primary out-of-fold predicted classes are present;
- all required primary out-of-fold probabilities are finite and within `[0, 1]`.

### 16.2 Baseline requirement

Let `BA_baseline` be the unweighted mean primary-fold balanced accuracy of the fold-trained majority baseline.

A candidate can be declared preferred only when its unweighted mean primary-fold balanced accuracy is strictly greater than `BA_baseline`.

When no eligible candidate exceeds the baseline, the recorded decision is:

`NO_CANDIDATE_EXCEEDED_FOLD_TRAINED_BASELINE`

No parameters are changed and no replacement model is introduced.

### 16.3 Ranking and practical tie

Among eligible candidates that exceed the baseline:

1. Find the highest unrounded mean primary-fold balanced accuracy.
2. Place every candidate within an absolute difference of `0.005000` from that maximum into the practical-tie set.
3. From the practical-tie set, choose the candidate with the lowest unrounded sample SD of fold balanced accuracy.
4. When two or more tied candidates have sample SD values within an absolute difference of `0.005000`, use this fixed interpretability order:
   1. logistic regression;
   2. decision tree;
   3. random forest.

Accuracy, F1, ROC-AUC, average precision and pooled metrics do not break ties.

The selected model is described as preferred for this pre-registered out-of-month label-reproduction comparison, not as a universally best wildfire model.

---

## 17. Warning, undefined-metric and failure handling

### 17.1 Warning capture

All Python warnings are captured with:

- timestamp;
- analysis variant;
- fold ID;
- model;
- warning category;
- exact message;
- action taken.

Warnings are not suppressed from the audit record.

### 17.2 Input or integrity failure

A failed checksum, schema check, label check, duplicate check, missing-value check or date check terminates the entire Phase 4B run with non-zero status. No estimator is fitted.

### 17.3 Model-fit failure

A fold is failed when:

- estimator fitting raises an exception;
- GLM does not report convergence;
- coefficients required for prediction are non-finite;
- predicted probabilities are missing, non-finite or outside `[0, 1]`;
- a fitted classifier lacks either encoded class `0` or `1`.

A failed fold is not retried with altered parameters. Predictions and metrics for that model/fold are recorded as missing with the exact error.

A candidate with any failed primary fold is ineligible for model preference.

### 17.4 Undefined threshold metrics

When a model predicts no positive cases, scikit-learn `zero_division=0` is applied to precision and F1 and the condition is recorded. This is not a fit failure.

Every planned primary held-out month is expected to contain both classes. If an implemented fold contains only one observed class, this contradicts the verified fold design and terminates the run rather than silently omitting ROC-AUC or average precision.

### 17.5 RQ2 failure

When an RQ2 specification fails to converge or yields non-finite required values:

- record the model as failed;
- do not change its specification;
- do not use a replacement estimator;
- do not perform an LRT requiring that model.

### 17.6 Permutation-importance failure

Permutation importance is calculated only for a successful primary random-forest fold. If any primary RF fold fails, the cross-fold permutation summary is missing and the failure is recorded. No training-set importance replaces it.

---

## 18. Exact logistic feature-contribution procedure

Feature contribution from logistic regression is descriptive and model-based.

After all primary LOMO predictions have been generated, fit one full-data primary logistic model using all 244 rows and the unchanged raw-Rain predictor specification.

Procedure:

1. Use predictors in the order:
   `Temperature`, `RH`, `Ws`, `Rain`.
2. Fit StandardScaler on all 244 rows:
   - `with_mean=True`;
   - `with_std=True`;
   - `ddof=0`.
3. Transform all predictors.
4. Add an intercept.
5. Fit the exact unpenalised statsmodels GLM in Section 11.
6. Save the full-data means and scales.
7. For each coefficient, save:
   - coefficient `β`;
   - standard error;
   - Wald `z`;
   - two-sided model-based p-value;
   - odds ratio `exp(β)`;
   - 95% Wald CI for `β`;
   - 95% Wald CI for the odds ratio.
8. Calculate the 95% CI using:
   `β ± 1.959963984540054 × SE`.
9. Interpret each weather-predictor odds ratio per one full-data population-standard-deviation increase.
10. Exclude the intercept from the report figure but retain it in the CSV.
11. Do not average coefficients across folds.
12. Label intervals:
   `ordinary model-based Wald intervals; not adjusted for temporal dependence`.
13. Do not interpret magnitude or direction causally.

This full-data fit does not replace cross-validated performance and cannot alter the preferred-model rule.

---

## 19. Exact held-out random-forest permutation importance

Permutation importance is calculated separately on each held-out month using that fold’s already-fitted primary random forest.

Implementation:

- function: `sklearn.inspection.permutation_importance`
- scoring: `balanced_accuracy`
- `n_repeats=30`
- `n_jobs=1`
- predictor order: `Temperature`, `RH`, `Ws`, `Rain`
- held-out data only
- no training-set importance
- no impurity-based importance
- no partial dependence

Fixed permutation seeds:

| Fold | Seed |
|---|---:|
| `F06` | `1406` |
| `F07` | `1407` |
| `F08` | `1408` |
| `F09` | `1409` |

For each fold, feature and repeat, save:

`importance = held-out balanced accuracy before permutation − held-out balanced accuracy after permutation`

Aggregation:

1. Within each fold and feature:
   - arithmetic mean across 30 repeats;
   - sample SD across 30 repeats (`ddof=1`).
2. Across folds and feature:
   - unweighted mean of the four fold-specific mean importances;
   - sample SD of the four fold-specific mean importances (`ddof=1`).
3. Cross-fold summary is produced only when all four fold-specific results are finite.

Negative importance values are retained. Correlated predictors can divide or suppress importance; no correction, grouping or conditional permutation is added.

Permutation importance is a model-dependent predictive contribution measure and is not physical or causal fire importance.

---

## 20. Final RQ2 specification table

RQ2 is analysed on all 244 rows. It is not cross-validated.

### 20.1 Coding and centring

- `region_sidi = 1` for `Sidi-Bel Abbes`
- `region_sidi = 0` for `Bejaia`
- target mapping remains `fire = 1`, `not fire = 0`
- continuous variables are mean-centred using arithmetic full-data means:
  - `Temperature_c = Temperature − mean(Temperature)`
  - `RH_c = RH − mean(RH)`
  - `Ws_c = Ws − mean(Ws)`
  - `Rain_c = Rain − mean(Rain)`

No scaling by standard deviation is used in RQ2.

### 20.2 Estimator

Every RQ2 model uses:

- `statsmodels.api.GLM`
- Binomial family
- logit link
- intercept included
- no penalty
- no weights
- IRLS
- `maxiter=200`
- `tol=1e-8`
- `cov_type="nonrobust"`

### 20.3 Models

| ID | Status | Exact design matrix |
|---|---|---|
| `R0_REGION_ONLY` | Primary specification table | intercept + `region_sidi` |
| `R1_REGION_TEMP_RH` | Primary specification table | intercept + `region_sidi` + `Temperature_c` + `RH_c` |
| `R2_REGION_ALL_WEATHER` | Primary specification table | intercept + `region_sidi` + `Temperature_c` + `RH_c` + `Ws_c` + `Rain_c` |
| `R3_REGION_RAIN_INTERACTION` | Exploratory sensitivity only | intercept + `region_sidi` + `Temperature_c` + `RH_c` + `Ws_c` + `Rain_c` + (`region_sidi × Rain_c`) |

For each successful model, report:

- convergence status;
- number of observations;
- number of fitted parameters;
- log-likelihood;
- AIC;
- region coefficient;
- region standard error;
- region Wald z;
- region two-sided model-based p-value;
- region odds ratio;
- model-based 95% Wald CI for region coefficient and odds ratio.

For R3, the region coefficient is the regional contrast at mean Rain and the other centred weather values. The interaction coefficient is the change in the regional log-odds contrast per 1 mm increase in Rain relative to the full-data mean.

AIC is reported across specifications but does not select one definitive causal or inferential answer.

---

## 21. RQ2 interaction and likelihood-ratio-test rules

Exactly one likelihood-ratio test is planned:

- reduced model: `R2_REGION_ALL_WEATHER`
- full model: `R3_REGION_RAIN_INTERACTION`
- degrees of freedom: `1`
- statistic:
  `D = 2 × (logLik_R3 − logLik_R2)`
- p-value:
  upper-tail probability from `χ²(df=1)`
- planned alpha:
  `0.050000`

Numerical rule:

- when `D >= 0`, use D unchanged;
- when `-1e-8 <= D < 0`, set `D = 0` as numerical tolerance and record this action;
- when `D < -1e-8`, mark the LRT failed because the nested-fit likelihood ordering is inconsistent.

Both R2 and R3 must converge with finite log-likelihoods. Otherwise, the LRT is not calculated.

Interpretation rule:

- `p < 0.05`: report evidence that adding the exploratory Region × Rain term improves in-sample fit under the specified models;
- `p >= 0.05`: report insufficient evidence that the exploratory interaction improves in-sample fit.

R3 remains an exploratory sensitivity regardless of p-value and never replaces the primary three-model specification table.

RQ2 outputs cannot support claims that region causes the designation, that weather mediates a causal effect, or that non-significance proves no association.

---

## 22. RQ3 confirmation

RQ3 remains fully descriptive.

Phase 4B performs:

- no RQ3 model;
- no forecast;
- no new FWI aggregation;
- no new class-proportion calculation;
- no new RQ3 figure.

The final report uses the frozen Phase 3 results and:

- Figure C: monthly class-designation proportions by region;
- Figure D: weekly mean FWI by region, with the first W-Sun bin identified as a three-day partial week.

No frozen Phase 3 file or figure is regenerated.

---

## 23. Final two-figure allocation

The assessment permits no more than five diagrams or screenshots. Frozen Figures B, C and D occupy three slots. The final two slots are fixed as follows.

### Figure 4 — `fig_4_rq1_lomo_balanced_accuracy.png`

Content:

- x-axis: held-out month in order June, July, August, September;
- y-axis: balanced accuracy from `0.0` to `1.0`;
- one point series for:
  - fold-trained majority baseline;
  - primary raw-Rain logistic regression;
  - decision tree;
  - random forest;
- no Rain-any sensitivity;
- no boundary-gap sensitivity;
- horizontal reference line at `0.5`;
- no confidence intervals;
- title states “out-of-month class-designation reproduction”;
- generated entirely from `fold_metrics.csv`.

### Figure 5 — `fig_5_rq1_logistic_odds_ratios.png`

Content:

- full-data primary logistic weather-predictor odds ratios;
- predictors: Temperature, RH, Ws, Rain;
- 95% ordinary model-based Wald intervals;
- logarithmic odds-ratio x-axis;
- vertical reference line at odds ratio `1`;
- intercept excluded;
- caption states:
  `Intervals are ordinary model-based intervals and are not adjusted for temporal dependence. The target is an FWI/FFMC-derived designation.`
- generated entirely from `logistic_full_data_coefficients.csv`.

No ROC curve, calibration plot, partial-dependence plot, confusion-matrix graphic or RQ2 figure is allocated.

---

## 24. Exact Phase 4B output manifest

Every output must be written under:

`04_Phase_4_Modelling_Working/`

| Filename | Required content |
|---|---|
| `phase4b_modelling.py` | Single executable implementation of this passed pre-registration |
| `PHASE4B_MODEL_SPECIFICATION.json` | Exact input paths, predictor orders, fold rules, gap dates, parameters, seeds, threshold, metrics, tie rule and failure rules |
| `PHASE4B_REQUIREMENTS.txt` | Exact pinned Python package versions from Section 25 |
| `PHASE4B_ENVIRONMENT.json` | Python version, package versions, platform, CPU/thread environment variables and run timestamp |
| `input_checksums.csv` | Filename, logical authoritative path, expected SHA-256, observed SHA-256 and pass/fail |
| `PHASE4B_RUN_LOG.txt` | Main execution record, followed only after manifest finalisation by the manifest filename, manifest SHA-256, final run status and final completion timestamp; intentionally excluded from the manifest |
| `warnings_and_failures.csv` | Timestamp, stage, variant, fold, model, category, message and action |
| `fold_assignments.csv` | Long-format source-row assignments for primary and gap analyses |
| `baseline_training_counts.csv` | Variant, fold, permitted training rows, fire count, not-fire count, fire prevalence and selected majority |
| `preprocessing_parameters.csv` | Variant, fold, model, feature, training mean, training scale and transformation |
| `oof_predictions.csv` | Variant, fold, source row, date, region, true label, model, predicted class, fire probability and status |
| `fold_metrics.csv` | Variant, fold, model, all fixed metrics, confusion counts and status |
| `metric_summary.csv` | Variant, model, metric, four-fold mean, sample SD, fold count and eligibility |
| `pooled_oof_metrics.csv` | Variant, model, pooled metrics and source-row count |
| `pooled_confusion_matrices.csv` | Variant, model, actual class, predicted class and pooled count |
| `model_selection_decision.json` | Baseline mean BA, eligible candidates, practical-tie set, tie-break fields and final decision |
| `rain_binary_sensitivity_metrics.csv` | Filtered Rain-any logistic fold, summary and pooled results |
| `boundary_gap_sensitivity_metrics.csv` | Filtered gap baseline/logistic/tree/RF fold, summary and pooled results |
| `logistic_full_data_coefficients.csv` | Intercept and weather coefficients, scaler values, SEs, z, p, ORs and model-based CIs |
| `permutation_importance_by_fold.csv` | Fold, feature, repeat, seed, baseline BA, permuted BA and decrease |
| `permutation_importance_summary.csv` | Fold-level and across-fold means/SDs for each feature |
| `rq2_centering_values.csv` | Full-data arithmetic means used for RQ2 centring |
| `rq2_specification_results.csv` | R0–R2 fit statistics and region estimates |
| `rq2_interaction_sensitivity.csv` | R3 estimates plus the fixed R2-versus-R3 LRT result |
| `fig_4_rq1_lomo_balanced_accuracy.png` | Final report Figure 4 |
| `fig_5_rq1_logistic_odds_ratios.png` | Final report Figure 5 |
| `PHASE4B_README.md` | How to run, authoritative inputs, outputs, interpretation restrictions and audit status |
| `PHASE4B_MANIFEST.csv` | Relative path, purpose, status, file size and SHA-256 for every Phase 4B artefact except `PHASE4B_MANIFEST.csv` and `PHASE4B_RUN_LOG.txt` |

Rules:

- All numeric tables and figures are generated by code.
- No manual alteration of generated values, labels or visual marks is permitted.
- A failed run must not be presented as complete; partial outputs remain clearly marked and are retained for audit.

### 24.1 Exact manifest and run-log finalisation procedure

1. Complete and finalise all numerical outputs, configuration files, CSV files, figures, documentation and every other Phase 4B artefact.
2. Finalise the main execution content of `PHASE4B_RUN_LOG.txt`, but do not yet add the manifest hash or the final completion record.
3. Generate `PHASE4B_MANIFEST.csv`.
4. The manifest must cover every Phase 4B artefact except:
   - `PHASE4B_MANIFEST.csv`;
   - `PHASE4B_RUN_LOG.txt`.
5. For every included artefact, record:
   - relative path;
   - purpose;
   - status;
   - file size;
   - SHA-256.
6. Finalise and write `PHASE4B_MANIFEST.csv`.
7. Compute the SHA-256 of the completed manifest.
8. Append to `PHASE4B_RUN_LOG.txt`:
   - the manifest filename;
   - the manifest SHA-256;
   - the final run status;
   - the final completion timestamp.
9. Do not alter or regenerate `PHASE4B_MANIFEST.csv` after its hash has been written to the run log.
10. The run log is intentionally excluded from the manifest because it is the final file written and contains the manifest hash.

---

## 25. Software, seeds and deterministic execution

Phase 4B must use:

- Python `3.13.5`
- NumPy `2.3.5`
- pandas `2.2.3`
- SciPy `1.17.0`
- statsmodels `0.14.6`
- scikit-learn `1.8.0`
- matplotlib `3.10.8`

Exact runtime controls:

- master seed: `140`
- Python `random.seed(140)`
- NumPy `numpy.random.seed(140)`
- decision-tree `random_state=140`
- random-forest `random_state=140`
- permutation seeds: `1406`, `1407`, `1408`, `1409`
- pre-interpreter process or shell environment: `PYTHONHASHSEED=140`
- pre-interpreter process or shell environment: `OMP_NUM_THREADS=1`
- pre-interpreter process or shell environment: `MKL_NUM_THREADS=1`
- pre-interpreter process or shell environment: `OPENBLAS_NUM_THREADS=1`
- pre-interpreter process or shell environment: `NUMEXPR_NUM_THREADS=1`
- random-forest and permutation `n_jobs=1`
- matplotlib backend: `Agg`
- matplotlib configuration directory: a writable directory inside `04_Phase_4_Modelling_Working/`

`PYTHONHASHSEED`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS` and `NUMEXPR_NUM_THREADS` must be established in the process or shell environment before the Python interpreter starts. The Python script must read and record their observed values in `PHASE4B_ENVIRONMENT.json` and the run log. Setting or changing these variables inside the already-running Python process does not retroactively control interpreter hashing or libraries that were initialised at startup, and the implementation must not claim otherwise.

The implementation command, current working directory, platform string and all observed versions and environment-variable values are written to `PHASE4B_ENVIRONMENT.json` and the run log.

No version substitution is authorised before audit. A version mismatch terminates the run and requires a revised audited environment decision.

---

## 26. Checksum, frozen-file and finalisation controls

At Phase 4B start:

1. Read `MASTER_MANIFEST.csv`.
2. Recompute SHA-256 for every available frozen input used.
3. Verify the cleaned CSV, Phase 3 frozen summary and Phase 3 frozen script against their manifest hashes.
4. Record hashes for:
   - `MASTER_MANIFEST.csv`;
   - `RELEASE_NOTES.md`;
   - `PHASE4_HANDOFF.md`;
   - `PHASE4A_REVISED_PREREGISTRATION.md` — the sole canonical Phase 4A implementation authority; calculate and record its SHA-256;
   - `ChatGPT_Phase4A_Audit.md.txt`;
   - `Claude_Phase4A_Original.md.txt`.
5. Do not require a manifest match for Phase 4 working documents that post-date the frozen Phase 1–3 package; save their observed hashes.
6. Never write to a frozen input path.
7. Never use a file from `99_Superseded_File_List/Archive_Do_Not_Use/`.
8. Never reconstruct unavailable `clean_forest_fires.py`, audit records, frozen figures or other missing authoritative files.
9. Write all Phase 4 outputs only to `04_Phase_4_Modelling_Working/`.

A manifest mismatch, frozen-path write attempt or prohibited archive reference closes the run.

Input checksum verification occurs before fitting. Output hashing and finalisation occur only after all Phase 4B artefacts are complete and must follow Section 24.1 exactly. `PHASE4B_MANIFEST.csv` excludes itself and `PHASE4B_RUN_LOG.txt`; the completed manifest is hashed once, and that hash is appended to the run log together with the final status and completion timestamp. The manifest must not be altered after that append. The run log remains outside the manifest because it is deliberately the final file written.

---

## 27. Interpretation and reporting restrictions

All Phase 4B and final-report language must comply with these rules:

- Use `class designation`, `recorded class`, `label reproduction` and `out-of-month label-reproduction performance`.
- Do not call `Classes` observed wildfire incidence.
- Do not describe RQ1 as validated real-fire prediction or future forecasting.
- A false negative means a failure to reproduce a `fire` designation, not a missed real wildfire.
- Do not interpret model coefficients or permutation importance causally.
- Do not interpret the region coefficient causally.
- Do not claim non-significance proves no regional association.
- Label RQ2 intervals as ordinary model-based intervals that may be optimistic because temporal dependence is unmodelled.
- Bound conclusions to Bejaia and Sidi-Bel Abbes during June–September 2012.
- Preserve the frozen Phase 3 wording and numerical findings.
- Preserve report anonymity.
- Respect each 300-word report-section maximum.
- Use no more than the five fixed report visuals: frozen B, C, D and Phase 4 Figures 4 and 5.

---

## 28. Remaining limitations

1. The target was derived from FWI and FFMC rather than independent fire observations.
2. The exact class-assignment thresholds are undocumented.
3. Raw weather is computationally related to FFMC; strong RQ1 performance would still be internal label reproduction.
4. The dataset contains only 244 observations.
5. It covers two regions and one June–September season.
6. Daily records are temporally dependent.
7. Four monthly folds provide limited precision for variability estimates.
8. Class prevalence differs across months.
9. Same-date regional rows are grouped in the same fold but are not independent replications of different dates.
10. The primary LOMO design retains adjacency at month boundaries; the fixed gap sensitivity checks but does not eliminate all temporal dependence.
11. Ordinary full-data logistic intervals do not adjust for temporal dependence.
12. Correlation between weather predictors can destabilise coefficients and divide permutation importance.
13. Decision-tree structures can be unstable in small samples.
14. Random-forest importance is model-dependent and ordinary permutation importance is affected by correlated predictors.
15. RQ2 region estimates are known from Phase 3 to be specification-dependent.
16. AIC and the planned LRT describe fitted-model evidence and do not establish causal truth.
17. The repaired record remains in the authoritative dataset; Phase 3 found no material sensitivity to its exclusion.
18. No external dataset or independently observed wildfire outcome is available for validation.
19. The five-visual assessment limit leaves only two Phase 4 figure slots.
20. The 300-word methods and results limits require detailed reproducibility evidence to remain in supporting files.

---

## 29. Prohibited deviations after audit

After this pre-registration receives PASS, the builder must not:

- change folds or gap dates;
- change a predictor or representation;
- change scaling;
- tune or replace an estimator;
- change any parameter, seed or threshold;
- introduce class weights or resampling;
- add random CV;
- add calibration, Brier score, partial dependence or a new analysis branch;
- use sensitivity results for primary model selection;
- change the preferred-model rule;
- omit failed folds;
- regenerate or modify frozen Phase 3 files;
- change the two-figure allocation after seeing results;
- manually edit generated numerical outputs or figures.

A necessary deviation discovered during implementation must stop Phase 4B and return to independent audit with a revised pre-registration.

---

## 30. Audit gate and next action

This document authorises no model fitting.

The next action is:

> Submit `PHASE4A_REVISED_PREREGISTRATION.md` to `02_Phase4_Auditor` for an independent audit against `PHASE4_HANDOFF.md`, the frozen inputs and all ten blocking corrections.

Phase 4B can begin only after the auditor gives an explicit **PASS**.

**Phase 4A revised plan ready for final independent audit.**
