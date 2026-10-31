# FINAL REPORT Q4 — ANALYTICAL TECHNIQUES AND EVALUATION CRITERIA DRAFT

## Analytical techniques and evaluation criteria

RQ1 evaluated reproduction of the recorded class designation through four grouped leave-one-month-out folds, holding out June, July, August and September in turn. This preserved temporal grouping instead of randomly mixing observations (Roberts et al., 2017). Preprocessing was learned from each training fold only. A fold-trained majority baseline was compared with preregistered unpenalised logistic regression, a shallow decision tree and a fixed random forest. Logistic regression supports interpretable binary-response associations, while trees represent nonlinear partitions and random forests aggregate randomised trees (Hosmer, Lemeshow and Sturdivant, 2013; Breiman et al., 1984; Breiman, 2001). Random cross-validation, tuning and threshold optimisation were prohibited.

Balanced accuracy was primary because monthly class proportions varied and it weights class-specific performance equally (Brodersen et al., 2010). Secondary metrics were accuracy, fire precision, fire recall, fire F1, not-fire recall, ROC-AUC, average precision and confusion counts. Metrics were recorded for each held-out month, as an unweighted four-fold mean with sample SD, and as pooled out-of-fold summaries. Candidates had to exceed the fold-mean baseline; mean balanced accuracy, 0.005 practical tie, SD and fixed interpretability order set preference. `Rain_any` and the three-day boundary-gap analysis were sensitivity checks excluded from model selection. Standardised logistic coefficients/odds ratios and held-out random-forest permutation importance were non-causal; importance was model-dependent (scikit-learn developers, n.d.).

RQ2 combined an unadjusted region–class contingency analysis with R0 (region only), R1 (Temperature/RH adjusted), R2 (all four weather variables adjusted) and exploratory R3 (Region × Rain). Model-based odds ratios, ordinary model-based 95% confidence intervals and AIC described specifications; a likelihood-ratio test compared R2 with R3. Inference remains specification-dependent and non-causal.

RQ3 used regional monthly class proportions and weekly mean FWI descriptively, without forecasting or causal modelling. Mann–Whitney tests and numerical Cliff’s δ supported exploratory comparisons where distributions were skewed or outlier-prone, but did not remove temporal-dependence concerns.

---

## Draft control record

**Exact word count:** 300 words, including the section heading and in-text citations. The document title and this control record are excluded.

**Methodological citations used:**
- `(Roberts et al., 2017)` — M-05, supporting temporally/group-structured validation.
- `(Hosmer, Lemeshow and Sturdivant, 2013)` — M-01, supporting binary logistic modelling and adjusted association summaries.
- `(Breiman et al., 1984)` — M-02, supporting decision-tree classification.
- `(Breiman, 2001)` — M-03, supporting random-forest classification.
- `(Brodersen et al., 2010)` — M-04, supporting balanced accuracy as equal weighting of class-specific performance.
- `(scikit-learn developers, n.d.)` — M-06, supporting the mechanics and model dependence of permutation importance.

**Frozen evidence files used:**
- `04_Phase_4_Modelling_Frozen/PHASE4A_REVISED_PREREGISTRATION.md`
- `04_Phase_4_Modelling_Frozen/PHASE4_FROZEN_SUMMARY.md`
- `05_Audit_Records/PHASE4B_COMPUTATIONAL_AUDIT.md`
- `04_Phase_4_Modelling_Frozen/PHASE4B_MODEL_SPECIFICATION.json`
- `04_Phase_4_Modelling_Frozen/model_selection_decision.json`
- `04_Phase_4_Modelling_Frozen/fold_assignments.csv`
- `04_Phase_4_Modelling_Frozen/fold_metrics.csv`
- `04_Phase_4_Modelling_Frozen/metric_summary.csv`
- `04_Phase_4_Modelling_Frozen/pooled_oof_metrics.csv`
- `04_Phase_4_Modelling_Frozen/rain_binary_sensitivity_metrics.csv`
- `04_Phase_4_Modelling_Frozen/boundary_gap_sensitivity_metrics.csv`
- `04_Phase_4_Modelling_Frozen/rq2_specification_results.csv`
- `04_Phase_4_Modelling_Frozen/rq2_interaction_sensitivity.csv`
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`
- `FINAL_REPORT_EVIDENCE_MAP.md`
- `FINAL_REPORT_REFERENCE_REGISTER.md`
- Frozen assessment brief, rubric and answer template

**Compliance check:**
- The section is within the 300-word maximum.
- Techniques are separated from performance-evaluation and model-comparison criteria.
- No model-performance value, preferred-model outcome, coefficient estimate, odds ratio, AIC value or likelihood-ratio result was introduced.
- Every method and rule described was frozen and audited; no method, parameter, threshold or evaluation criterion was invented or changed.
- No visual was added; Figures 4 and 5 remain reserved for the results section.
- Sensitivity analyses are explicitly excluded from model selection.
- Logistic summaries and permutation importance are identified as non-causal, and RQ2 inference as specification-dependent.
