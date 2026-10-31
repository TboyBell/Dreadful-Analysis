# FINAL REPORT Q2 — EXPLORATORY DATA ANALYSIS DRAFT

## Exploratory data analysis

I explored Temperature, relative humidity, wind speed, rainfall and FWI through summary statistics and distribution plots, then examined weather variables by recorded class, region-by-month class proportions, and weekly mean FWI. The recorded classes comprised 138 `fire` and 106 `not fire` observations. Pooled and within-region Mann–Whitney comparisons with Cliff’s δ and Holm adjustment were used because rainfall was zero-heavy and several distributions contained outliers; results were interpreted cautiously because daily observations may be temporally dependent.

Figure B shows the clearest class-related meteorological patterns. Observations assigned `fire` were generally warmer and less humid, while rainfall was concentrated near zero. Frozen pooled δ values were 0.607 for Temperature, −0.494 for relative humidity and −0.725 for rainfall; wind speed showed little separation (−0.023). These are associations with an FWI/FFMC-derived designation, not independently observed wildfire incidence (Abid and Izeboudjen, 2020).

![](fig_B_weather_by_class.png)

**Figure B.** Temperature, relative humidity, rainfall and wind speed by recorded class designation.

Monthly proportions varied by region and season (Figure C). Both regions were highest in August (Bejaia 24/31; Sidi-Bel Abbes 27/31), while September fell to 7/30 and 16/30 respectively. These proportions are descriptive and are not fire-occurrence rates.

![](fig_C_monthly_class_proportion.png)

**Figure C.** Monthly proportions assigned the `fire` class in each region.

Weekly mean FWI rose to a shared late-August peak before falling sharply (Figure D). A zero-rain run preceded and continued through that peak, but similar dry runs elsewhere did not produce a comparable peak; therefore, no causal conclusion is justified. The first weekly aggregate was partial.

![](fig_D_fwi_weekly_trend.png)

**Figure D.** Weekly mean FWI by region; the first week is partial.

The EDA therefore supported class-aware evaluation, temporal validation, regional adjustment and sensitivity checks. Registered model candidates were not selected after viewing their outcomes.

---

## Draft control record

**Exact word count:** 281 words. This includes the report-section heading, prose, in-text citation and all three substantive figure captions. It excludes the document title, Markdown image-link syntax and this control record.

**Frozen evidence files used:**
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`
- `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_README.md`
- `03_Phase_3_EDA_Frozen/fig_B_weather_by_class.png`
- `03_Phase_3_EDA_Frozen/fig_C_monthly_class_proportion.png`
- `03_Phase_3_EDA_Frozen/fig_D_fwi_weekly_trend.png`
- `FINAL_REPORT_EVIDENCE_MAP.md`
- Frozen assessment brief, rubric and answer template

**Frozen values used:**
- Class counts: 138 `fire`, 106 `not fire`
- Pooled Cliff’s δ: Temperature 0.607; relative humidity −0.494; rainfall −0.725; wind speed −0.023
- August class counts: Bejaia 24/31; Sidi-Bel Abbes 27/31
- September class counts: Bejaia 7/30; Sidi-Bel Abbes 16/30
- Frozen qualitative findings on zero-heavy rainfall, outliers, temporal dependence, the shared late-August weekly FWI peak, the accompanying zero-rain run and the partial first week

**Citation used:**
- `(Abid and Izeboudjen, 2020)` — controlled reference BG-02, used only for class-construction context.

**Compliance check:**
- The exact Q2 wording and excellent-level rubric requirements in the approved evidence map governed the draft.
- The section is below the 300-word maximum, with captions included conservatively.
- Only frozen Phase 3 numerical findings were used; no calculations were rerun and no new statistics were created.
- Figures B, C and D are the approved Q2 visuals and each appears exactly once.
- The text distinguishes the recorded FWI/FFMC-derived designation from independently observed wildfire incidence.
- No causal claim, Phase 4 result, cleaning detail or unapproved reference was introduced.
- The EDA-to-analysis link is described without claiming outcome-driven model selection.
