# Phase 3 — EDA (FROZEN)

## How to run
```
python3 phase3_frozen.py --input <path-to-cleaned-csv> --outdir <output-directory>
```

## Command-line arguments
- `--input` — path to the Phase 2 cleaned CSV (default:
  `Algerian_forest_fires_dataset_CLEANED.csv` in the working directory)
- `--outdir` — directory to write figures to; created automatically if it
  doesn't exist (default: current directory)

## Expected input
The Phase 2 frozen cleaned dataset (244 rows × 17 columns) from
`../02_Phase_2_Cleaning_Frozen/Algerian_forest_fires_dataset_CLEANED.csv`.

## Expected outputs
- Printed console output: pooled and per-region descriptive statistics,
  Mann-Whitney tests, Cliff's delta with Holm correction, the multiple-
  testing family-choice check, rain zero-value handling, the three-model
  regional logistic comparison, autocorrelation results, repaired-record
  sensitivity, and the zero-rain streak calculation.
- Three figure files: `fig_B_weather_by_class.png`,
  `fig_C_monthly_class_proportion.png`, `fig_D_fwi_weekly_trend.png`.

## Required Python packages
See `requirements.txt` (pandas, numpy, scipy, statsmodels, matplotlib).

## Purpose of each figure
- **Figure B** — Temperature/RH/Rain/Ws by recorded class (boxplots, full
  units). Evidences RQ1.
- **Figure C** — Monthly class-designation proportion by region, descriptive
  only (no confidence intervals, since daily records are not an independent
  sample). Evidences RQ2 and RQ3.
- **Figure D** — Weekly mean FWI trend by region across the season.
  Evidences RQ3.

## Candidates for the final report
Figures B, C and D are the current recommendation. Figure A (class balance)
and Figure E (DMC/DC/BUI multicollinearity, standardised by region) were
produced during analysis but are held out of the report — A because the
138/106 split can be stated in text, E because it's only relevant if the
modelling section discusses feature redundancy.

**Three of the maximum five report figure slots are currently allocated
(B, C, D), leaving two free for modelling-phase results.**

## Audit status
**Phase 3 passed final independent audit and is frozen.**
