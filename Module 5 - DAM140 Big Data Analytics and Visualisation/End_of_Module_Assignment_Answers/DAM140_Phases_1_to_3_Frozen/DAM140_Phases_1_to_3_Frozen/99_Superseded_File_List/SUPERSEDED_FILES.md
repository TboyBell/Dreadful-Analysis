# Superseded Files — Do Not Use

All files below are preserved in `Archive_Do_Not_Use/` for traceability only.
None should be used for the report, further analysis, or Phase 4.

| File | Why superseded |
|---|---|
| `phase3_final.py` | Second-generation Phase 3 script; superseded by `phase3_frozen.py`, which fixed the missing pooled-comparison call, added auto-mkdir, corrected wording, and shortened clipped figure labels |
| `phase3_revised_analysis.py` | First-generation Phase 3 script; superseded by later corrections (target provenance, effect-size interpretation, regional model comparison, Figure C, dry-spell reproducibility) |
| `eda_analysis.py` | Earliest, pre-audit EDA script; entirely superseded |
| `chart1_class_balance.png` through `chart6_multicollinearity_illustration.png` | Original draft EDA figures from before the first audit round; superseded by the corrected Figure A–E set, which was itself later narrowed to B/C/D |
| `fig_A_class_balance.png` | Held out of the final report by decision (counts can be stated in text), not because it was wrong |
| `fig_C_fire_rate_region_month_CI.png` | Superseded — used Wilson confidence intervals on temporally dependent daily records, which was identified as statistically inappropriate and removed in the frozen version |
| `fig_D_fwi_seasonal_trend_neutral.png` | Superseded by the current `fig_D_fwi_weekly_trend.png` (shortened, unclipped y-axis label) |
| `fig_E_multicollinearity_by_region.png` | Not incorrect, but excluded from the current report figure set; reserved for possible use in a later modelling-technique discussion |

## Superseded prose (no separate file existed)

One superseded *sentence* was identified and corrected mid-conversation:

> "Pooled and per-region comparisons show Temperature, RH and Rain each show
> a large-magnitude association with the class designation (Cliff's δ ≥
> 0.49 in every case)."

This was inaccurate because the Bejaia-subgroup RH result is medium
(δ = −0.451), not large. It was corrected in the Phase 3 summary text at
the time it was identified. This sentence was never saved as a standalone
file in the workspace (only as chat text), so there is no separate file to
archive for it — it is recorded here for completeness, and the corrected
wording is what appears in `03_Phase_3_EDA_Frozen/PHASE3_FROZEN_SUMMARY.md`.
