# FINAL REPORT EVIDENCE MAP — CORRECTED CANONICAL VERSION

**Project:** DAM140 Big Data Analytics and Visualization Assessment  
**Chat role:** `03_Final_Report`  
**Authoritative archive:** `DAM140_Phases_1_to_4_Frozen.zip`  
**Companion source register:** `FINAL_REPORT_REFERENCE_REGISTER.md`  
**Purpose:** evidence mapping, authority control and drafting preparation only. This document is not a draft of the final assessment answers and contains no new analytical finding.

> **SOURCE-AUTHORITY RULE — CONTROLLING:** The frozen archive is the sole authority for project data, computations, figures and analytical conclusions. Verified external academic, technical, regulatory and legal sources may be used only for background justification, methodology, scalable architecture, privacy, legislation and Harvard referencing. External sources must not alter or replace frozen analytical evidence.

---

## 1. Archive and authority verification

### 1.1 Archive integrity

- The uploaded ZIP opened, listed and extracted successfully.
- `unzip -t` reported no compressed-data errors.
- Extracted root: `DAM140_Phases_1_to_4_Frozen/`.
- The package contains 72 files.
- `CHECKSUMS_SHA256.txt` contains 71 recorded checksums; every recorded checksum verified as **OK**.
- `MASTER_MANIFEST.csv` contains 70 file records plus its header.
- Manifest status distribution: 57 `authoritative/frozen`; 13 `superseded - archived, not authoritative`.
- Manifest `final_report_use` distribution: 20 permitted report-evidence files; 37 supporting-only files; 13 prohibited superseded files.
- The archive contains the assessment brief, answer template, grading rubric, cleaned data and cleaning script, frozen Phase 3 summary and figures, frozen Phase 4 outputs and figures, computational audit, reference documentation, audit decisions and superseded-file registers.

### 1.2 Frozen analytical status

- Phase 2 passed and is frozen.
- Phase 3 passed and is frozen.
- Phase 4A passed design audit and is frozen.
- Phase 4B was accepted with minor non-blocking package corrections.
- Final status: **PASS — Phase 4 frozen release accepted**.
- No model fitting, prediction, metric, coefficient, permutation-importance result, RQ2 result or figure was recalculated during final assembly or this correction stage.

### 1.3 Controlling authority order

1. The current instruction and the source-authority rule above.
2. `MASTER_MANIFEST.csv`, especially `final_report_use`.
3. `RELEASE_NOTES.md` and `05_Audit_Records/PHASE4_FINAL_AUDIT_STATUS.md`.
4. `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md` for frozen Phase 3 findings.
5. `04_Phase_4_Modelling_Frozen/PHASE4_FROZEN_SUMMARY.md` for report-ready Phase 4 conclusions and restrictions.
6. Permitted frozen numerical tables and the five approved figures.
7. `05_Audit_Records/PHASE4B_COMPUTATIONAL_AUDIT.md` for verification, diagnostics and interpretation restrictions.
8. Supporting-only scripts, specifications, manifests and logs for provenance—not alternative conclusions.
9. `FINAL_REPORT_REFERENCE_REGISTER.md` only for the permitted external roles stated in the authority rule.

Anything under `99_Superseded_File_List/Archive_Do_Not_Use/` is prohibited for report writing.

---

## 2. Frozen research questions

Use these versions **exactly**, including terminology and scope:

**RQ1:** How accurately can Temperature, relative humidity, wind speed and rainfall reproduce the dataset’s FWI/FFMC-derived class designation, and which of these meteorological variables contribute most to that classification?

**RQ2:** Does the association between region and the recorded FWI/FFMC-derived class designation persist after adjustment for the measured meteorological variables?

**RQ3:** How do FWI values and the proportion of observations assigned the fire class vary across Bejaia and Sidi-Bel Abbes during June–September 2012?

Do not substitute abbreviated questions, change the target to observed wildfire incidence, describe RQ1 as wildfire forecasting, or make RQ3 inferential.

---

## 3. Assessment-section table

The grading rubric allocates 4 points to each of seven marked criteria, total 28 points. Q8 is mandatory in the answer template but has no separate rubric row.

| ID | Exact assessment question | Maximum | Excellent-level rubric requirement | Approved support | Figure allocation |
|---|---|---:|---|---|---|
| Q1 | “Investigate given data and state the three business or research questions that you would like to answer through your analysis and justify why they are interesting” | 300 words | State all three clearly and justify them using relevant external background resources. | Assessment brief/template; exact frozen RQs; Phase 3 summary; BG-01–BG-04 under the authority rule. | None. |
| Q2 | “Describe how you explored/visualized the data, why you did it that way, and what conclusions you drew about it” | 300 words | Explain what was explored, how and why; give clear conclusions with relevant support. | Phase 3 summary/README; Figures B, C and D; supporting Phase 3 script; BG-02/BG-03 only for target/FWI background. | Figures B, C and D, each once. |
| Q3 | “Describe the cleaning/fixing you did on the data, and why” | 300 words | Clearly explain cleaning/handling methods and why they were selected. | Phase 2 README; cleaning script; cleaned CSV; Phase 2 audit; BG-01 for provenance only. | None. |
| Q4 | “Explain what analysis techniques and evaluation criteria you used to answer your business/research questions and for evaluating the performance of the analysis techniques, and why” | 300 words | Describe techniques/evaluation clearly and justify them with relevant methodological sources. | Phase 4 preregistration/summary/audit; frozen result tables; Phase 3 descriptive methods; M-01–M-06 selectively. | No duplicate figure placement; refer to Figures 4/5 only if they are placed later in Q5. |
| Q5 | “Summarise the results of your analysis. What do the results say in answer to your business/research questions?” | 300 words | Convincingly answer all three RQs, discuss implications and give proportionate further suggestions. | Frozen Phase 3/4 summaries; permitted numerical tables; Figures 4 and 5; refer back to Figures C/D rather than repeat them. | Figures 4 and 5, each once. |
| Q6 | “Imagine that you have to deal with a much larger version of this dataset, with gigabytes of data already held and tens of megabytes of new data arriving each day. Assume that rapid response to new data is required e.g. certain messages being sent immediately as soon as certain automated analysis results produce results of a certain value (e.g. a count of items of a particular type exceeds a predetermined threshold). Describe a way that you could use appropriate technologies to spread the load over multiple computers and justify why this would be a good approach.” | 300 words | Propose and justify distribution across multiple computers, parallel load, high-velocity response and suitable technologies. | Assessment scenario/rubric plus A-01–A-08 selectively. This is a proposal, not a completed implementation. | None. |
| Q7 | “Imagine that this data will be used in support of a public-facing application. List the three most salient privacy issues related to this analysis and give strategies you could use to address each of them.” | 300 words | Discuss exactly three issues; tie each to applicable legislation/regulatory principles and a concrete mitigation. | Assessment prompt/rubric; L-01–L-06; declared hypothetical application assumptions. | None. |
| Q8 | “Provide a correctly structured list of references to all the resources used for this development and report” | No word limit | Use accurate Harvard references for every source actually cited. | Archive reference README/PDF; controlled register; R-01; only sources used in the report. | None. |
| Submission | Official delivery and anonymity requirements | N/A | Mandatory compliance. | Assessment brief, answer template and grading-schema pages. | Maximum five visuals in the whole document. |

---

## 4. Detailed evidence-to-question mapping

## Q1 — Research questions and justification

### Exact research questions

Use the three questions in Section 2 verbatim. Do not shorten them in the answer.

### Approved project files

- `00_Assessment_Documents/BDAV_Final_Assessment_Report__July_2026_docx-1.docx`.
- `00_Assessment_Documents/DAM140_Final_Assignment_Answer_Template-1.docx`.
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`.
- `04_Phase_4_Modelling_Frozen/PHASE4A_REVISED_PREREGISTRATION.md`.
- `04_References/BOOK_Chapter_Springer_ABID.pdf`.
- `04_References/REFERENCES_README.md`.

### Approved factual basis

- 244 observations, 122 per region, June–September 2012.
- 138 `fire` designations and 106 `not fire` designations.
- The original source describes assignment to the two classes using FWI and FFMC; exact assignment thresholds are undocumented.
- RQ1 is an out-of-month label-reproduction question using four meteorological variables rather than the FWI/FFMC components used in constructing the recorded target.
- RQ2 asks whether a region–designation association persists across the registered adjustment specifications.
- RQ3 uses the dataset’s two-region/four-month structure descriptively.

### Approved external sources and precise role

- BG-01: official dataset provenance, variables, observation counts and time/region scope.
- BG-02: original accompanying chapter and class-construction context.
- BG-03: optional FWI-system background only.
- BG-04: optional evidence that later work has analysed the same dataset; not independent validation of this project’s regional conclusions.

### Interpretation limitations and prohibited claims

- `Classes` is an FWI/FFMC-derived designation, not independently observed wildfire incidence.
- Do not describe the project as predicting, detecting or forecasting real wildfires.
- Do not imply that the undocumented target thresholds were recovered.
- Do not use same-dataset external studies as independent confirmation of the frozen results.

### Ambiguity status

- The former external-authority gap is resolved by the source-authority rule and controlled register.
- Exact target thresholds remain unknown and must be stated as a limitation if relevant.

---

## Q2 — Exploratory data analysis and visualisation

### Approved files

- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`.
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_README.md`.
- `03_Phase_3_EDA_Frozen/fig_B_weather_by_class.png`.
- `03_Phase_3_EDA_Frozen/fig_C_monthly_class_proportion.png`.
- `03_Phase_3_EDA_Frozen/fig_D_fwi_weekly_trend.png`.
- `03_Phase_3_EDA_Frozen/phase3_frozen.py` as supporting-only provenance.

### Approved EDA methods

- Pooled and within-region comparisons of Temperature, relative humidity, wind speed and rainfall by recorded class.
- Mann–Whitney comparisons and numerical Cliff’s delta values, with Holm adjustment.
- Explicit treatment of zero-heavy rainfall.
- **Unadjusted region–class contingency analysis plus three logistic specifications: region only, Temperature/RH-adjusted, and all-four-weather-adjusted.**
- R0 is region only.
- R1 adjusts for Temperature and RH.
- R2 adjusts for all four weather variables.
- R3 is a **separate exploratory Region × Rain interaction sensitivity**, not one of the three main logistic specifications.
- Weekly mean FWI aggregation by calendar week ending Sunday; the first week is partial.
- Autocorrelation checks and warning that daily observations are temporally dependent.
- Repaired-record sensitivity and deterministic zero-rain-streak analysis.

### Approved findings

- Temperature: pooled Cliff’s δ = 0.607.
- Relative humidity: pooled δ = −0.494; Bejaia-specific δ = −0.451.
- Wind speed: pooled δ = −0.023.
- Rainfall: pooled δ = −0.725.
- **Do not attach Romano-style qualitative magnitude terms** to these values unless that source is later authoritatively verified.
- Unadjusted region–class result: χ² = 6.02, p = 0.014, Cramér’s V = 0.157.
- Figure C labels:
  - Bejaia: 13/30 June, 15/31 July, 24/31 August, 7/30 September.
  - Sidi-Bel Abbes: 12/30 June, 24/31 July, 27/31 August, 16/30 September.
- A zero-rain run began before and continued through the late-August FWI peak week in both regions; comparable dry runs elsewhere did not produce a comparable peak.
- The repaired record had no material effect on the frozen findings.

### Figure allocation

- Figure B appears once in Q2: weather variables by recorded class designation.
- Figure C appears once in Q2: monthly proportions assigned the `fire` class by region.
- Figure D appears once in Q2: weekly mean FWI trends by region.
- Q5 may refer back to Figures C/D but must not reproduce them.

### References

- BG-02 for target provenance.
- BG-03 only if the FWI system’s structure is described.
- Romano magnitude terminology is prohibited pending verification.

### Interpretation limitations and prohibited claims

- Figure C is descriptive; do not add confidence intervals or treat daily observations as independent binomial samples.
- Figure C is not wildfire incidence or occurrence rate.
- Figure D is weekly mean FWI, not a count/rate of fires.
- Do not claim the late-August peak was caused by the dry run.
- Do not reinstate excluded/superseded Figures A, C, D or E.
- Do not estimate exact weekly FWI point values from the plot.

---

## Q3 — Data cleaning

### Approved files

- `02_Phase_2_Cleaning_Frozen/PHASE2_FROZEN_README.md`.
- `02_Phase_2_Cleaning_Frozen/clean_forest_fires.py` as supporting implementation evidence.
- `02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`.
- `02_Phase_2_Cleaning_Frozen/PHASE2_MANIFEST.csv`.
- `05_Audit_Records/PHASE2_AUDIT_DECISION.txt`.

### Approved cleaning operations

- Validate embedded raw headers rather than substitute an unverified header.
- Split the two embedded regional blocks and add `Region`.
- Strip whitespace and standardise data types.
- Standardise target labels to `fire` and `not fire`.
- Construct a calendar `date` column.
- Repair one structurally malformed record and flag it with `record_repaired=True`.
- Enforce validation checks with assertions.

### Approved numerical findings

- Final shape: 244 records × 17 attributes.
- Fourteen original fields plus `Region`, `date` and `record_repaired`.
- 0 missing values and 0 duplicate rows.
- Two regions with 122 records each; two standardised class labels.
- Dates from 1 June to 30 September 2012.
- Exactly one reconstructed record.
- Repaired record: 14 July 2012, Sidi-Bel Abbes; plausible split recorded as DC = 14.6 and ISI = 9.

### Reference role

- BG-01 may support source provenance only. All cleaning operations and counts come from the frozen archive.

### Interpretation limitations

- The repaired split is plausible, not a verified recovery of the missing comma.
- Cleaning did not create or independently validate the class designation.
- Do not modify, regenerate or substitute the authoritative cleaned CSV.

---

## Q4 — Analytical techniques and evaluation criteria

### Approved files

- `04_Phase_4_Modelling_Frozen/PHASE4A_REVISED_PREREGISTRATION.md`.
- `04_Phase_4_Modelling_Frozen/PHASE4_FROZEN_SUMMARY.md`.
- `05_Audit_Records/PHASE4B_COMPUTATIONAL_AUDIT.md`.
- `04_Phase_4_Modelling_Frozen/model_selection_decision.json`.
- Frozen metric/model tables, including `fold_metrics.csv`, `metric_summary.csv`, `pooled_oof_metrics.csv`, `pooled_confusion_matrices.csv`, sensitivity tables, coefficient/importance tables and RQ2 tables.
- Frozen Phase 3 summary for RQ3’s descriptive techniques.

### RQ1 techniques and design controls

- Four-fold leave-one-month-out evaluation: June, July, August and September are held out in turn.
- Fold-contained preprocessing and a fold-trained majority-class baseline.
- Registered primary candidates: standardised logistic regression with raw Rain, decision tree and random forest.
- Selection metric: unweighted mean four-fold balanced accuracy.
- Fixed practical-tie threshold 0.005, followed by registered fold-SD and interpretability tie rules.
- Pooled out-of-fold metrics are supplementary and not interchangeable with the fold-mean selection metric.
- `Rain_any` logistic model is a preregistered sensitivity and did not participate in model selection.
- Three-day boundary-gap analysis is a separate sensitivity.
- Full-data standardised logistic coefficients are post-validation explanatory summaries with ordinary model-based Wald intervals.
- Held-out random-forest permutation importance uses balanced-accuracy decrease, 30 repeats per fold; it is fitted-model/data/scoring-rule dependent and non-causal.

### Leave-one-month-out fold register

| Fold | Training | Test | Test fire | Test not fire |
|---|---:|---:|---:|---:|
| June | 184 | 60 | 25 | 35 |
| July | 182 | 62 | 39 | 23 |
| August | 182 | 62 | 51 | 11 |
| September | 184 | 60 | 23 | 37 |

### RQ2 techniques

- **Unadjusted region–class contingency analysis plus three logistic specifications: region only, Temperature/RH-adjusted, and all-four-weather-adjusted.**
- R0: region only.
- R1: adjusts for Temperature and RH.
- R2: adjusts for all four weather variables.
- R3: separate exploratory Region × Rain interaction sensitivity.
- Intervals are ordinary model-based intervals not adjusted for temporal dependence.

### RQ3 techniques

- Descriptive monthly class proportions and weekly mean FWI trends from frozen Phase 3.
- No Phase 4 model was added for RQ3.

### Evaluation criteria and source roles

- M-04 supports balanced accuracy as equal weighting of class-specific performance.
- M-05 supports grouped/temporally structured validation rather than random mixing of dependent observations.
- M-01 supports binary logistic modelling and adjusted odds-ratio interpretation.
- M-02 and M-03 support decision-tree/random-forest method descriptions.
- M-06 supports the mechanics and limitations of permutation importance.
- Use only the minimum subset needed for a concise 300-word explanation.

### Figure control

- Do not place Figures 4 or 5 here if they are allocated to Q5.
- Q4 may describe the evaluation design and refer to the later approved figures without duplicating them.

### Interpretation limitations

- RQ1 is out-of-month reproduction of a recorded designation, not validated wildfire forecasting.
- Random forest was selected among the registered primary candidates.
- `Rain_any` was a preregistered sensitivity, not a selection candidate.
- Rain’s logistic coefficient is sensitive to sparse influential observations.
- Permutation importance is model-dependent and non-causal; negative wind importance is not a protective effect.
- RQ2 is specification-dependent; non-significance is not proof of no regional association.
- R3 is exploratory and unstable.

---

## Q5 — Results mapped to RQ1, RQ2 and RQ3

### RQ1 approved result map

- Selected primary model: random forest.
- Four-fold mean balanced accuracy and sample SD:
  - baseline 0.500, SD 0.000;
  - logistic regression with raw Rain 0.742, SD 0.077;
  - decision tree 0.838, SD 0.061;
  - random forest 0.853, SD 0.049.
- Random-forest balanced accuracy by held-out month: June 0.909; July 0.822; August 0.880; September 0.802.
- Random-forest pooled out-of-fold metrics: accuracy 0.873; balanced accuracy 0.867; precision 0.869; recall 0.913; F1 0.890; ROC-AUC 0.944; average precision 0.934.
- Random-forest pooled confusion counts: 87 `not fire` correctly reproduced; 19 `not fire` reproduced as `fire`; 12 `fire` reproduced as `not fire`; 126 `fire` correctly reproduced.
- Boundary-gap sensitivity: random-forest mean balanced accuracy 0.844; primary ordering/conclusion stable.
- `Rain_any` sensitivity: mean balanced accuracy 0.857, SD 0.035; pooled balanced accuracy 0.875; excluded from model selection.
- Mean held-out permutation importance: Rain 0.2766; RH 0.0334; Temperature 0.0247; Ws −0.0060.
- Full-data standardised logistic odds ratios and intervals: Temperature 3.046 (1.802–5.150); RH 0.517 (0.321–0.834); Ws 1.351 (0.913–2.000); Rain 0.00721 (0.00084–0.0619).

#### Required RQ1 controls

- State that the random forest was selected among registered primary candidates.
- Rain was the largest held-out permutation contribution, but importance is model-dependent and non-causal.
- Rain’s logistic coefficient is sensitive to sparse influential observations.
- Do not convert Rain’s odds ratio into real-wildfire risk reduction.
- A false negative means failure to reproduce a `fire` designation, not a missed wildfire.

### RQ2 approved result map

Method description to use: **Unadjusted region–class contingency analysis plus three logistic specifications: region only, Temperature/RH-adjusted, and all-four-weather-adjusted.**

- Unadjusted contingency: χ² = 6.02, p = 0.014, Cramér’s V = 0.157.
- R0 region only: OR 1.962, 95% interval 1.173–3.280, p 0.0102, AIC 331.342.
- R1 adjusts for Temperature and RH: OR 0.995, interval 0.526–1.881, p 0.9879, AIC 261.399.
- R2 adjusts for all four weather variables: OR 1.724, interval 0.830–3.577, p 0.1440, AIC 204.225.
- Approved conclusion: the regional result is specification-dependent; the adjustment sequence does not yield one definitive adjusted region estimate.
- Separate exploratory R3 Region × Rain sensitivity: log-likelihood −77.4173; AIC 168.835; R2-vs-R3 likelihood-ratio statistic 37.3906; p approximately 9.67 × 10⁻¹⁰.
- R3’s coefficients/odds ratios are extreme under sparse, near-separating rainfall patterns and are not suitable for detailed substantive interpretation.

#### Required RQ2 controls

- Do not claim weather definitively explains away the region association.
- Do not treat non-significance as proof of no association.
- Do not interpret region causally.
- Label intervals as ordinary model-based intervals not adjusted for temporal dependence.
- Treat R3 as exploratory instability evidence, not a precise physical effect.

### RQ3 approved result map

- RQ3 remains entirely descriptive and uses frozen Phase 3 findings.
- Monthly labels are those in Figure C.
- Both regions have their highest displayed `fire`-class proportions in August; Sidi-Bel Abbes is higher in July, August and September, while June is similar.
- Weekly FWI in both regions reaches a late-August peak; the plotted Sidi-Bel Abbes peak is higher.
- A zero-rain run spans the peak week in both regions, but other dry runs do not yield comparable peaks.

#### Required RQ3 controls

- Confine conclusions to Bejaia and Sidi-Bel Abbes during June–September 2012.
- Say “proportion assigned the fire class,” not wildfire incidence/rate.
- Do not infer causes or calculate new statistics.
- Do not estimate weekly FWI values from Figure D.

### Figure allocation

- Figure 4 appears once in Q5 for leave-one-month-out balanced accuracy.
- Figure 5 appears once in Q5 for standardised logistic odds ratios.
- Refer back to Figures C/D for RQ3; do not duplicate them.

---

## Q6 — Scalable big-data architecture

### Status and authority

Q6 is a proposed scalable architecture, not an implementation completed in this project. It was not deployed, benchmarked or tested in this project. The assessment scenario is authoritative for requirements; verified external technical documentation may justify proposed components only.

### Scenario requirements

- Gigabytes of retained data.
- Tens of megabytes of new data per day.
- Rapid threshold-triggered messages.
- Load distributed over multiple computers.
- Rubric emphasis on parallelism, shared load, multiple servers/processors and high-velocity response.

### Permitted proposed component map

| Function | Permitted proposed component | External basis | Drafting control |
|---|---|---|---|
| Ingestion/event buffer | Partitioned Kafka topics across brokers | A-01 | Describe durable distributed event ingestion; do not claim it was installed. |
| Distributed storage | HDFS replicated blocks across DataNodes | A-02 | Justify large retained datasets and node-failure tolerance; do not claim project data required HDFS. |
| Distributed processing | Spark Structured Streaming for incremental rules/features; Spark batch where appropriate | A-03 | State processing guarantees conditionally and accurately; avoid unconditional “exactly once”. |
| Batch orchestration | Airflow DAGs for scheduled retraining/data-quality/batch workflows | A-04 | Keep Airflow out of the immediate alert latency path. |
| Model/API deployment and scaling | Containerised service on Kubernetes worker nodes | A-05 | Proposed deployment only; scaling depends on configured resources/metrics. |
| Operational monitoring/alerts | Prometheus metrics and Alertmanager | A-06 | Monitoring of services/model pipeline, distinct from the application’s domain threshold alerts. |
| Security/governance | Kubernetes Secrets encryption/least privilege and RBAC | A-07, A-08 | Include authentication, least privilege, secret management and auditability; no claim of completed hardening. |

### Required answer logic

- Explain the end-to-end flow from ingestion to distributed storage/processing, threshold state, alert delivery and monitoring.
- Explain partitioning/parallelism and how extra workers can share load.
- Explain fault tolerance and recovery without promising zero downtime.
- Compare the proposal with a single-machine/single-process approach for the hypothetical scale and latency requirement.
- Standardise the brief’s “two computers” and rubric’s “multiple computers” as a multi-node design with at least two worker computers.

### Prohibited claims

- The project deployed, benchmarked, load-tested or security-tested this architecture.
- The 244-row frozen analysis required big-data infrastructure.
- A product guarantee follows from documentation alone.
- The architecture produced any frozen project result.
- An architecture diagram is added; all five visual slots are allocated to approved analytical figures.

### Remaining ambiguity

- Vendor/cloud deployment, exact node counts, throughput targets, retention volume and alert service are hypothetical. State reasonable assumptions succinctly rather than present them as implemented facts.

---

## Q7 — Three privacy issues, legislation and mitigations

### Legal-context control

- Use a UK public-facing application context for the assessment response, explicitly identified as an assumption because the prompt does not specify jurisdiction.
- Current framework: UK GDPR and Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025. The DUAA amends rather than replaces the existing framework, and its data-protection provisions were in force by 19 June 2026.
- The frozen meteorological CSV has no named individuals. Privacy issues arise only if the hypothetical application processes personal data such as precise location, account/device identifiers, alert subscriptions, usage logs or linked histories.

### Exactly three controlled issue mappings

| Privacy issue | Why it arises in the hypothetical application | Specific legal/regulatory principle | Concrete mitigation | Authoritative sources |
|---|---|---|---|---|
| 1. Excessive collection of precise location, account or device identifiers | A location-aware alert service could collect data more granular or persistent than needed to deliver regional information; linked identifiers can make records personal and reveal routines. | UK GDPR Article 5(1)(c), data minimisation; implement data protection by design/default where relevant. | Default to coarse region rather than precise coordinates; make precise location optional and purpose-bound; avoid permanent device IDs where a rotating/pseudonymous token works; document necessity for each field; separate identity from analytical records. | L-01, L-02, L-03, L-04 |
| 2. Indefinite retention and re-identifiable history | Location/search/alert histories and server logs can accumulate and permit profiling or re-identification after the operational purpose has ended. | UK GDPR Article 5(1)(e), storage limitation. | Set field-specific retention periods; automatically delete raw histories/logs when no longer needed; aggregate or anonymise longer-term statistics; review retention and deletion evidence periodically. | L-01, L-02, L-03, L-05 |
| 3. Unauthorised access, disclosure or loss | Linking accounts, locations and alert histories creates confidentiality and availability risks from compromised credentials, excessive privileges, insecure APIs or failed recovery. | UK GDPR Article 5(1)(f), integrity/confidentiality, and Article 32 risk-appropriate security. | Encrypt in transit and at rest; use MFA for administrators, RBAC/least privilege, key rotation and secure secrets; log/admin-monitor access; patch/test systems; maintain tested backups, restoration and incident-response procedures. | L-01, L-02, L-03, L-06 |

### Drafting controls

- Exactly three issues—do not add a fourth generic issue.
- For each issue include the application data flow, legal principle, why it matters and concrete resolution.
- Do not write “follow GDPR” without naming the provision/principle and mitigation.
- Do not assert that the frozen dataset itself contains personal data.
- Do not give definitive legal advice; frame the answer as design/compliance analysis for the hypothetical application.
- Do not invent implemented application features.

### Remaining ambiguity

- The controller, lawful basis, users, alert channels and exact data flows are hypothetical. The three mappings above establish explicit minimal assumptions for drafting.

---

## Q8 — Harvard references

### Controlling register

- `FINAL_REPORT_REFERENCE_REGISTER.md` is the controlled external-source register.
- The archive remains authoritative for project evidence; external references support only their permitted roles.
- Use only sources actually cited in the final report.

### Harvard controls

- Use author–date in-text citations and a corresponding alphabetised reference list.
- Verify author/institution, year, title, publisher/journal, volume/issue/pages and DOI or official URL.
- Include an access date for web documentation/guidance where the required Harvard variant expects one.
- Include page numbers for direct quotations and precise passage-level paraphrases where required.
- Maintain one consistent Harvard variant, with the module/template’s rules controlling over R-01 if they differ.
- Do not fabricate page numbers, quotations, publication details or unavailable full-text verification.
- Do not list unused sources merely because they appear in the controlled register.
- Romano magnitude terminology and its citation remain excluded unless an authoritative source is later verified.

---

## 5. Five-figure allocation

The report permits no more than five visuals. Each approved figure may appear only once. Later sections may refer back to a figure rather than duplicate it. Substantive caption text should be counted conservatively within the relevant 300-word limit.

| Slot | Approved visual | Single placement | Permitted later cross-reference | Restrictions |
|---:|---|---|---|---|
| 1 | Figure B — weather variables by class designation | Q2 | Q4/Q5 may refer back | Recorded designation language only. |
| 2 | Figure C — monthly class proportions by region | Q2 | Q5 RQ3 refers back | Descriptive; proportion assigned the `fire` class, not incidence. |
| 3 | Figure D — weekly FWI trend by region | Q2 | Q5 RQ3 refers back | Weekly mean FWI; no causal interpretation or visual value extraction. |
| 4 | Figure 4 — leave-one-month-out balanced accuracy | Q5 | None required | Primary models/baseline only; sensitivity models intentionally absent. |
| 5 | Figure 5 — standardised logistic odds ratios | Q5 | None required | Ordinary model-based intervals; Rain requires influential-observation caution. |

No ROC curve, confusion-matrix graphic, RQ2 graphic, architecture/privacy diagram, Figure A, Figure E or superseded visual may be added without replacing an approved figure and re-auditing the limit.

---

## 6. Approved numerical-results register

All numbers are frozen. The register does not require every value to appear within 300-word sections.

| Topic | Approved values | Controlling evidence |
|---|---|---|
| Dataset | 244 records; 122 per region; 138 `fire`, 106 `not fire`; June–September 2012 | BG-01/BG-02 for provenance; frozen Phase 2/3 summaries for project use |
| Cleaned data | 244 × 17; 0 missing; 0 duplicates; one flagged repaired record; DC 14.6 and ISI 9 plausible reconstruction | Phase 2 README/audit |
| Pooled class contrasts | Temperature δ 0.607; RH δ −0.494; Ws δ −0.023; Rain δ −0.725; Bejaia RH δ −0.451 | Phase 3 summary; report numerically, no unverified magnitude labels |
| Unadjusted region association | χ² 6.02; p 0.014; Cramér’s V 0.157 | Phase 3 summary |
| Monthly class labels | Bejaia 13/30, 15/31, 24/31, 7/30; Sidi-Bel Abbes 12/30, 24/31, 27/31, 16/30 | Figure C |
| Primary mean balanced accuracy | Baseline 0.500; logistic 0.742; tree 0.838; forest 0.853 | Metric summary/audit |
| Random-forest held-out months | June 0.909; July 0.822; August 0.880; September 0.802 | Fold metrics/Figure 4/audit |
| Random-forest pooled metrics | Accuracy 0.873; BA 0.867; precision 0.869; recall 0.913; F1 0.890; ROC-AUC 0.944; AP 0.934 | Pooled OOF metrics/audit |
| Rain-any sensitivity | Mean BA 0.857; SD 0.035; pooled BA 0.875 | Sensitivity table/audit |
| Boundary-gap forest | Mean BA 0.844 | Boundary-gap table/audit |
| Permutation importance | Rain 0.2766; RH 0.0334; Temperature 0.0247; Ws −0.0060 | Permutation table/audit |
| Logistic ORs | Temperature 3.046; RH 0.517; Ws 1.351; Rain 0.00721, with registered intervals | Coefficient table/Figure 5/audit |
| RQ2 R0 region only | OR 1.962; p 0.0102; AIC 331.342 | RQ2 table |
| RQ2 R1 Temperature/RH-adjusted | OR 0.995; p 0.9879; AIC 261.399 | RQ2 table |
| RQ2 R2 all-four-weather-adjusted | OR 1.724; p 0.1440; AIC 204.225 | RQ2 table |
| R3 exploratory Region × Rain | LRT 37.3906; p 9.67 × 10⁻¹⁰; unstable sparse interaction | RQ2 sensitivity/audit |

### Leave-one-month-out sample register

| Fold | Training | Test | Test fire | Test not fire |
|---|---:|---:|---:|---:|
| June | 184 | 60 | 25 | 35 |
| July | 182 | 62 | 39 | 23 |
| August | 182 | 62 | 51 | 11 |
| September | 184 | 60 | 23 | 37 |

### Numbers not to foreground

- R3’s extreme region/interaction odds ratios.
- A real-wildfire percentage interpretation of Rain’s logistic odds ratio.
- Pooled baseline BA around 0.367 as though it contradicted fold-mean baseline BA 0.500; they are different aggregations.
- Exact weekly FWI values inferred from Figure D.

---

## 7. Approved terminology register

### Use

- FWI/FFMC-derived class designation.
- Recorded class / recorded designation.
- `fire` designation / `not fire` designation.
- Label reproduction; out-of-month label-reproduction performance.
- Proportion of observations assigned the fire class.
- Association / model-based association.
- Unadjusted region–class contingency analysis plus three logistic specifications.
- R0 region only; R1 Temperature/RH-adjusted; R2 all-four-weather-adjusted.
- Separate exploratory Region × Rain interaction sensitivity (R3).
- Model-dependent permutation contribution.
- Random forest selected among the registered primary candidates.
- `Rain_any` preregistered sensitivity, excluded from model selection.
- Ordinary model-based interval, not adjusted for temporal dependence.
- Specification-dependent regional result.
- Descriptive RQ3 findings.
- Proposed scalable architecture / hypothetical public-facing application.

### Error language

- “Failure to reproduce a `fire` designation.”
- “Failure to reproduce a `not fire` designation.”

Do not relabel errors as missed/false wildfire events.

### Magnitude terminology control

- Report Cliff’s delta numerically.
- Do not use Romano-derived “small”, “medium”, “large” or equivalent magnitude terminology unless the source is later verified and admitted through a controlled update.

---

## 8. Prohibited-claims register

Do not state or imply that:

- `Classes` records independently observed wildfire incidence.
- The project predicts, forecasts or detects real wildfires.
- Leave-one-month-out performance validates future wildfire forecasting.
- Exact FWI/FFMC class thresholds are known.
- Random forest was selected from every possible model rather than among registered primary candidates.
- `Rain_any` was selected or definitively superior.
- Four folds establish reliable superiority between close models.
- Rain’s logistic coefficient is stable, precise, physical or causal.
- Rain changes real-wildfire odds by a stated percentage.
- Permutation importance is causal, model-independent or a physical importance ranking.
- Negative Ws importance is protective.
- RQ2 proves presence/absence of a causal regional effect.
- Non-significance proves no association.
- R3’s extreme estimates are precise or substantively stable.
- Figure C is wildfire incidence, occurrence rate or independent binomial sampling.
- A zero-rain streak caused the late-August FWI peak.
- The repaired record was definitively corrected.
- A superseded/working/chat-transcoded file is authoritative.
- The scalable architecture was implemented, deployed, tested, benchmarked or used to obtain frozen results.
- The 244-row analysis required big-data infrastructure.
- The frozen meteorological CSV necessarily contains personal data.
- Generic “GDPR compliance” resolves a privacy issue without a provision and mitigation.
- Romano qualitative magnitude terminology is verified.
- External sources replace or change frozen project evidence.

---

## 9. Reference requirements and controlled status

| Section | Required support | Controlled status |
|---|---|---|
| Q1 | Dataset provenance, class context and concise background | Resolved: BG-01/BG-02 core; BG-03/BG-04 optional. |
| Q2 | Target/FWI context; project EDA remains internal | Resolved: BG-02/BG-03. Romano terminology excluded. |
| Q3 | Dataset provenance only | Resolved: BG-01. |
| Q4 | Balanced accuracy, temporal/grouped validation and named methods | Resolved: M-01–M-06; select minimally. |
| Q5 | Frozen internal results; target interpretation where needed | Resolved: frozen archive controls; BG-02 only for target boundary. |
| Q6 | Distributed ingestion/storage/processing/orchestration/deployment/monitoring/security | Resolved: A-01–A-08; proposed architecture only. |
| Q7 | Current UK framework plus issue-specific principles | Resolved: L-01–L-06; exactly three mapped issues. |
| Q8 | Accurate Harvard references for sources actually used | Resolved: controlled register plus R-01, subject to module’s Harvard variant. |

---

## 10. Submission-file requirements

### Mandatory report controls

- Use the supplied answer-template structure.
- Do not include the student’s name or another identifier in the document or filename.
- Submit a Canvas-displayable PDF or native Microsoft Word file as permitted by the brief.
- Q1–Q7: maximum 300 words each.
- Q8: no stated word limit.
- Cover page and reference list/bibliography are excluded from section limits.
- Maximum five visuals across the report.
- Each approved figure appears once; later sections cross-reference rather than duplicate.
- Count substantive caption text conservatively within the relevant 300-word limit.
- Use Harvard referencing consistently.

### Mandatory submitted files

- Completed final report.
- The cleaned CSV must be submitted separately, with attribute names in the first row:
  - `02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`.
- The brief states that failure to submit all required files results in zero for the assessment.

### Recorded Canvas details

- Due: 3 August at 22:00.
- Submission type: file upload.
- Four attempts recorded on the captured grading page.
- No student name in filename or document.

### Non-analytical format ambiguity

- The brief says PDF or native Microsoft Word; template wording mentions `.doc` or `.pdf` while the supplied template is `.docx`. Preserve the official template structure and use a Canvas-accepted format.

---

## 11. Unresolved or assumption-controlled issues before drafting

1. Exact FWI/FFMC class-assignment thresholds remain undocumented.
2. Exact weekly FWI point values are not available in a report-ready frozen table; do not infer them from Figure D.
3. Q6 node counts, cloud/on-premises choice, throughput targets, retention and alert channel are hypothetical; state assumptions and do not claim implementation.
4. Q7 controller, lawful basis and data flows are hypothetical; use the explicit UK/location-account-log assumptions in the controlled mapping.
5. The `.doc`/`.docx`/native-Word wording is not perfectly aligned; confirm the Canvas-accepted file type at submission.
6. Romano magnitude terminology remains prohibited unless an authoritative source is verified through a later controlled update.
7. The final reference list must be reduced to sources actually cited; the register itself is broader than the final list.

The former source-authority, methodology-source, architecture-source and privacy/legal-source gaps are resolved and are no longer drafting blockers.

---

## 12. Recommended drafting order

1. Lock the exact RQs, authority rule, terminology and prohibited-claims registers.
2. Reserve the five single-use figure placements and caption word allowance.
3. Draft Q3 from frozen cleaning evidence.
4. Draft Q2 around Figures B/C/D and numerical, non-Romano EDA wording.
5. Draft Q4 from the preregistered design, LOMO table and the minimum methodological references.
6. Draft Q5 in RQ1/RQ2/RQ3 order, using Figures 4/5 and referring back to C/D.
7. Draft Q1 using the exact RQs and concise BG-01/BG-02 justification.
8. Draft Q6 explicitly as a proposed multi-node architecture using a compact official-source set.
9. Draft Q7 using exactly the three controlled issue–law–mitigation mappings.
10. Build Q8 from sources actually cited, then audit every in-text citation against the list.
11. Run final QA: anonymity, seven 300-word limits, caption counting, five visuals once each, report file and separately uploaded cleaned CSV.

---

## 13. Audit correction table

| Audit issue | Correction made | File and section |
|---|---|---|
| Frozen RQ wording abbreviated | Replaced with the three exact canonical questions and prohibited later abbreviation. | `FINAL_REPORT_EVIDENCE_MAP.md`, Sections 2, 3 and Q1/Q5 controls |
| Regional-model description inaccurate | Replaced with “Unadjusted region–class contingency analysis plus three logistic specifications: region only, Temperature/RH-adjusted, and all-four-weather-adjusted”; defined R0, R1, R2 and separate exploratory R3. | `FINAL_REPORT_EVIDENCE_MAP.md`, Q2, Q4, Q5, terminology register |
| External-source authority gap | Added the controlling authority rule and limited external evidence to background, methods, architecture, privacy, legislation and referencing. | Both files, opening authority rule and usage controls |
| External references unverified/incomplete | Created a controlled register with full Harvard details, precise supported claims, authority reason, DOI/official URL, access date and full-text flags. | `FINAL_REPORT_REFERENCE_REGISTER.md` |
| Architecture could be mistaken for implementation | Marked Q6 as a proposed architecture; mapped permitted components and prohibited deployed/tested/benchmarked claims. | `FINAL_REPORT_EVIDENCE_MAP.md`, Q6 and prohibited-claims register |
| Privacy/legal mapping generic | Mapped exactly three issues to Article 5(1)(c), Article 5(1)(e), and Article 5(1)(f)/Article 32, with concrete mitigations and current UK sources. | `FINAL_REPORT_EVIDENCE_MAP.md`, Q7; reference register L-01–L-06 |
| LOMO fold register omitted | Added the exact training/test/class counts in Q4 and the numerical-results register. | `FINAL_REPORT_EVIDENCE_MAP.md`, Q4 and Section 6 |
| Figure/caption/submission controls incomplete | Required each figure once, later cross-reference only, conservative caption counting, and separate cleaned-CSV submission. | `FINAL_REPORT_EVIDENCE_MAP.md`, Sections 5 and 10 |
| Romano terminology unverified | Removed qualitative magnitude labels, excluded Romano from the controlled register, and retained numerical Cliff’s delta values only. | Both files, Q2/terminology controls and excluded-items table |

---

Evidence-map corrections and controlled external-source register complete; ready for final evidence-map re-audit.
