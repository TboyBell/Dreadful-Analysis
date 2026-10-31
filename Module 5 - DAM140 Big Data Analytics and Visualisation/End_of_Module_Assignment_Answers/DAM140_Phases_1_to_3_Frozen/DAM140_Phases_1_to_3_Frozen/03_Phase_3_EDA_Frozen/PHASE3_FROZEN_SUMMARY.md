# Phase 3 — Frozen Summary

## Target variable
`Classes` is an FWI/FFMC-derived class designation (Abid and Izeboudjen, 2020,
p. 367: the authors state the 244 instances were first assigned to "fire"
and "not fire" using the FWI system's FWI and FFMC components). The exact
threshold rule used to convert FWI/FFMC into the two classes is undocumented.
Later model performance (Phase 4) must not be interpreted as independently
validated wildfire prediction — it measures reproduction of this dataset's
class designation.

## Frozen research questions

1. How accurately can Temperature, relative humidity, wind speed and
   rainfall reproduce the dataset's FWI/FFMC-derived class designation, and
   which of these meteorological variables contribute most to that
   classification?
2. Does the association between region and the recorded FWI/FFMC-derived
   class designation persist after adjustment for the measured
   meteorological variables?
3. How do FWI values and the proportion of observations assigned the fire
   class vary across Bejaia and Sidi-Bel Abbes during June–September 2012?

## Corrected effect-size statement (authoritative wording)

> In the pooled analysis, Temperature, relative humidity and rainfall had
> large Cliff's delta magnitudes. The same statistical-significance pattern
> occurred within both regions, although the relative-humidity effect in
> Bejaia was medium (δ = −0.451) rather than large.

Numerical Cliff's delta values are primary; Romano et al. (2006) qualitative
categories are secondary description.

## Key pooled results
- Temperature: δ = 0.607 (large)
- RH: δ = −0.494 (large, pooled) — but medium in the Bejaia subgroup specifically
- Ws: δ = −0.023 (negligible)
- Rain: δ = −0.725 (large)
- Region–class association: χ²=6.02, p=0.014, Cramér's V=0.157 (small,
  unadjusted); the adjusted region coefficient is specification-dependent
  across three logistic models and no single adjusted estimate is treated
  as definitive.
- A zero-rain run begins before and continues through the late-August FWI
  peak week in both regions; comparable dry runs elsewhere in the season did
  not produce a comparable peak.
- One repaired record (flagged, `record_repaired=True`) was shown to have no
  material effect on any result.

## Audit status
**Phase 3 passed final independent audit and is frozen.** It must not be
changed unless a later phase reveals a genuine dependency error.
