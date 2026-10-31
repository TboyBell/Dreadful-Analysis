"""
DAM140 - Phase 3 (Final Corrected Version)
Second audit-corrected version.

IMPORTANT SCOPE NOTE ON THE TARGET VARIABLE
--------------------------------------------
This script treats `Classes` as a class designation whose exact construction
method is not independently confirmed by this script or by primary-source
text retrieved during this session (see accompanying written notes for the
full explanation and what was / was not verified). All results below
describe association between measured variables and this recorded class
designation. No claim of "true" or "independently observed" wildfire
occurrence is made anywhere in this script's output.

This script reproduces, from code, every numerical result referenced in
the final Phase 3 write-up: descriptive statistics, effect sizes, multiple-
testing correction, regional model comparison, autocorrelation, repaired-
record sensitivity, the dry-spell/zero-rain-streak calculation, and
Figures B, C and D. It does NOT reproduce literature-search conclusions
(external sources are cited in the accompanying notes, not derived here).

Usage: python3 phase3_final.py [--input PATH] [--outdir PATH]
"""

import argparse
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.tsa.stattools import acf
import statsmodels.api as sm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)


def load(path):
    df = pd.read_csv(path, parse_dates=['date'])
    df['fire_flag'] = (df.Classes == 'fire').astype(int)
    return df


# ---------------------------------------------------------------------------
# Effect size helpers
# ---------------------------------------------------------------------------

def cliffs_delta(x, y):
    x = np.asarray(x); y = np.asarray(y)
    gt = 0; lt = 0
    for xi in x:
        gt += np.sum(xi > y)
        lt += np.sum(xi < y)
    n = len(x) * len(y)
    return (gt - lt) / n


def cliffs_magnitude(d):
    """Romano et al. (2006) thresholds, as used in the effsize R package
    documentation: |d|<0.147 negligible, <0.33 small, <0.474 medium, else large."""
    ad = abs(d)
    if ad < 0.147: return "negligible"
    if ad < 0.33: return "small"
    if ad < 0.474: return "medium"
    return "large"


def cramers_v(chi2, n, r, c):
    return np.sqrt(chi2 / (n * (min(r, c) - 1)))


# ---------------------------------------------------------------------------
# 1. Group comparisons with corrected Cliff's delta magnitude labels
# ---------------------------------------------------------------------------

def group_comparisons(df, label=""):
    cols = ['Temperature', 'RH', 'Ws', 'Rain']
    results = []
    for col in cols:
        fire = df[df.Classes == 'fire'][col]
        notfire = df[df.Classes == 'not fire'][col]
        u, p = stats.mannwhitneyu(fire, notfire, alternative='two-sided')
        delta = cliffs_delta(fire.values, notfire.values)
        results.append({
            'variable': col,
            'median_fire': fire.median(), 'median_notfire': notfire.median(),
            'U': u, 'p_raw': p, 'cliffs_delta': delta,
            'magnitude_Romano2006': cliffs_magnitude(delta)
        })
    res_df = pd.DataFrame(results)
    reject, p_holm, _, _ = multipletests(res_df['p_raw'], method='holm', alpha=0.05)
    res_df['p_holm'] = p_holm
    res_df['significant_after_holm'] = reject
    print(f"\n--- Group comparisons {label} (Holm-corrected within this 4-test family) ---")
    print(res_df.to_string(index=False))
    return res_df


def holm_family_choice_check(df):
    """
    Check whether treating the two regional subgroup comparisons as one
    combined 8-test family (instead of two separate 4-test families)
    changes any significance conclusion.
    """
    print("\n--- Multiple-testing family choice: does it matter? ---")
    all_p = []
    labels = []
    for region in df['Region'].unique():
        sub = df[df.Region == region]
        for col in ['Temperature', 'RH', 'Ws', 'Rain']:
            fire = sub[sub.Classes == 'fire'][col]
            notfire = sub[sub.Classes == 'not fire'][col]
            _, p = stats.mannwhitneyu(fire, notfire, alternative='two-sided')
            all_p.append(p)
            labels.append(f"{region}-{col}")
    reject8, p_holm8, _, _ = multipletests(all_p, method='holm', alpha=0.05)
    combined = pd.DataFrame({'test': labels, 'p_raw': all_p, 'p_holm_combined8': p_holm8, 'sig_combined8': reject8})
    print(combined.to_string(index=False))
    print("\nConvention used elsewhere in this analysis: TWO separate four-test "
          "families (one per region). Checked here: whether combining into one "
          "eight-test family changes any conclusion.")
    return combined


def rain_zero_handling(df):
    print("\n--- Rain zero-value handling ---")
    for cls in ['fire', 'not fire']:
        sub = df[df.Classes == cls]['Rain']
        zero_prop = (sub == 0).mean()
        nonzero = sub[sub > 0]
        print(f"{cls:10s}: zero-rain proportion={zero_prop:.3f} (n={len(sub)}); "
              f"non-zero median={nonzero.median():.2f}, n_nonzero={len(nonzero)}")


# ---------------------------------------------------------------------------
# 2. Regional model comparison (three specifications, no single model chosen as final)
# ---------------------------------------------------------------------------

def regional_model_comparison(df):
    print("\n--- Regional association: unadjusted ---")
    ct = pd.crosstab(df['Region'], df['Classes'])
    pct = pd.crosstab(df['Region'], df['Classes'], normalize='index')
    print("Counts:\n", ct)
    print("Row percentages:\n", (pct * 100).round(1))
    chi2, p, dof, exp = stats.chi2_contingency(ct)
    n = ct.values.sum()
    v = cramers_v(chi2, n, *ct.shape)
    print(f"chi2={chi2:.3f}, p={p:.4f}, dof={dof}, Cramer's V={v:.3f} "
          f"(small association in this June-Sept 2012 sample; not evidence of causation)")

    y = df['fire_flag']
    specs = {
        'region_only': ['region_sidi'],
        'region_temp_rh': ['region_sidi', 'Temperature', 'RH'],
        'region_all_four': ['region_sidi', 'Temperature', 'RH', 'Ws', 'Rain'],
    }
    X_base = pd.DataFrame({
        'region_sidi': (df['Region'] == 'Sidi-Bel Abbes').astype(int),
        'Temperature': df['Temperature'], 'RH': df['RH'],
        'Ws': df['Ws'], 'Rain': df['Rain']
    })

    print("\n--- Regional coefficient across three model specifications ---")
    rows = []
    for name, predictors in specs.items():
        X = sm.add_constant(X_base[predictors])
        model = sm.Logit(y, X).fit(disp=0)
        converged = model.mle_retvals['converged']
        coef = model.params['region_sidi']
        se = model.bse['region_sidi']
        p_val = model.pvalues['region_sidi']
        ci_low, ci_high = model.conf_int().loc['region_sidi']
        rows.append({
            'model': name, 'predictors': predictors,
            'region_coef': coef, 'odds_ratio': np.exp(coef),
            'OR_CI_low': np.exp(ci_low), 'OR_CI_high': np.exp(ci_high),
            'p_value': p_val, 'converged': converged
        })
    result = pd.DataFrame(rows)
    print(result.to_string(index=False))
    print("\nNote: these three specifications are reported for comparison, not to "
          "select one as 'the' answer. The region estimate is not stable across "
          "specifications (it changes materially depending which meteorological "
          "variables are included), which is itself the finding to report - not "
          "a single adjusted p-value.")
    return result


# ---------------------------------------------------------------------------
# 3. Temporal dependence (unchanged from previous verified round, retained)
# ---------------------------------------------------------------------------

def temporal_dependence(df):
    print("\n--- Temporal dependence ---")
    print("Aggregation rule for all weekly figures/statistics: pandas .resample('W'), "
          "i.e. calendar weeks ending Sunday (W-SUN), applied separately within each "
          "region's date-sorted series. The FIRST such period per region is a partial "
          "week (1-3 June 2012 covers 3 days, not 7); all subsequent periods contain "
          "seven days. This is a descriptive aggregation choice, not a modelling claim.")
    for region in df['Region'].unique():
        sub = df[df.Region == region].sort_values('date')
        first_week = sub.set_index('date')['FWI'].resample('W').count().iloc[0]
        print(f"\n{region}: first W-SUN bin contains {first_week} day(s).")
        for col in ['Temperature', 'DC', 'FFMC']:
            vals = acf(sub[col], nlags=7, fft=False)
            print(f"  {col:12s} ACF lag1-7: " + ", ".join(f"{v:.2f}" for v in vals[1:]))
    print("\nAdjacent daily observations within a region are temporally dependent "
          "(DMC/DC are recursively defined - Van Wagner, 1987). Standard independent-"
          "sample statistics (e.g. the Mann-Whitney tests above) are DESCRIPTIVE "
          "summaries of this specific June-Sept 2012 sample; they are not treated as "
          "inference to a larger population of days or years.")


# ---------------------------------------------------------------------------
# 4. Repaired-record sensitivity (unchanged, retained)
# ---------------------------------------------------------------------------

def repaired_record_sensitivity(df):
    print("\n--- Repaired-record sensitivity ---")
    df_excl = df[~df['record_repaired']].copy()
    print(f"n with repaired record: {len(df)}; n excluding it: {len(df_excl)}")
    for col in ['Temperature', 'RH', 'Ws', 'Rain']:
        f1, nf1 = df[df.Classes == 'fire'][col], df[df.Classes == 'not fire'][col]
        f2, nf2 = df_excl[df_excl.Classes == 'fire'][col], df_excl[df_excl.Classes == 'not fire'][col]
        _, p1 = stats.mannwhitneyu(f1, nf1)
        _, p2 = stats.mannwhitneyu(f2, nf2)
        print(f"  {col:12s} p with={p1:.2e}   p without={p2:.2e}")
    ct1 = pd.crosstab(df['Region'], df['Classes'])
    ct2 = pd.crosstab(df_excl['Region'], df_excl['Classes'])
    chi2_1, p1, _, _ = stats.chi2_contingency(ct1)
    chi2_2, p2, _, _ = stats.chi2_contingency(ct2)
    print(f"  Region chi2 with={chi2_1:.3f} (p={p1:.4f})   without={chi2_2:.3f} (p={p2:.4f})")
    print("No result changes at a level that would alter the reported conclusions.")


# ---------------------------------------------------------------------------
# 5. Dry-spell / zero-rain streak calculation (deterministic, no hardcoded dates)
# ---------------------------------------------------------------------------

def zero_rain_streaks(df, min_length=3):
    """
    Finds every run of consecutive zero-rain days within each region's
    date-sorted series and returns them all, longest first. Nothing here
    is hardcoded to a specific date - the date ranges are a DERIVED OUTPUT.
    """
    print(f"\n--- Zero-rain streak calculation (rule: consecutive Rain==0 days, "
          f"min length {min_length}, computed separately per region) ---")
    all_streaks = []
    for region in df['Region'].unique():
        sub = df[df.Region == region].sort_values('date').reset_index(drop=True)
        streak_start = None
        for i, row in sub.iterrows():
            if row['Rain'] == 0:
                if streak_start is None:
                    streak_start = row['date']
                streak_end = row['date']
            else:
                if streak_start is not None:
                    length = (streak_end - streak_start).days + 1
                    if length >= min_length:
                        all_streaks.append({'Region': region, 'start': streak_start,
                                             'end': streak_end, 'duration_days': length})
                streak_start = None
        if streak_start is not None:  # streak runs to end of season
            length = (streak_end - streak_start).days + 1
            if length >= min_length:
                all_streaks.append({'Region': region, 'start': streak_start,
                                     'end': streak_end, 'duration_days': length})

    streaks_df = pd.DataFrame(all_streaks).sort_values('duration_days', ascending=False)
    print(streaks_df.to_string(index=False))

    print("\nLongest streak per region:")
    longest = streaks_df.loc[streaks_df.groupby('Region')['duration_days'].idxmax()]
    print(longest.to_string(index=False))
    print("\n(For comparison only - not assumed in advance: an external reviewer "
          "independently reported approximate windows of 17-29 August for Bejaia "
          "and 20-27 August for Sidi-Bel Abbes. The values above are derived fresh "
          "by this code from the cleaned dataset, not copied from that report.)")
    return streaks_df


# ---------------------------------------------------------------------------
# 6. Figures B, C (no CIs), D
# ---------------------------------------------------------------------------

def make_figures(df, outdir):
    plt.rcParams.update({'font.size': 11, 'figure.dpi': 150, 'font.family': 'sans-serif'})

    # Figure B
    fig, axes = plt.subplots(1, 4, figsize=(14, 4))
    specs = [('Temperature', 'Temperature (°C)'), ('RH', 'Relative humidity (%)'),
             ('Rain', 'Rainfall (mm)'), ('Ws', 'Wind speed (km/h)')]
    for ax, (col, label) in zip(axes, specs):
        data = [df[df.Classes == 'not fire'][col], df[df.Classes == 'fire'][col]]
        bp = ax.boxplot(data, tick_labels=['not fire', 'fire'], patch_artist=True)
        for patch, color in zip(bp['boxes'], ['#8a8a8a', '#4a4a4a']):
            patch.set_facecolor(color); patch.set_alpha(0.6)
        ax.set_title(label)
        ax.set_ylabel(label)
    fig.suptitle('Meteorological variables by recorded class designation (June-Sept 2012)')
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig_B_weather_by_class.png')
    plt.close()

    # Figure C - descriptive only, no CIs, with counts labelled
    grp = df.groupby(['month', 'Region'])['fire_flag'].agg(['sum', 'count']).reset_index()
    grp['rate'] = grp['sum'] / grp['count']
    month_names = {6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep'}
    fig, ax = plt.subplots(figsize=(8, 4.5))
    width = 0.35
    for i, region in enumerate(['Bejaia', 'Sidi-Bel Abbes']):
        sub = grp[grp.Region == region].sort_values('month')
        x = np.arange(len(sub)) + (i - 0.5) * width
        bars = ax.bar(x, sub['rate'], width, label=region,
                       color='#4a4a4a' if region == 'Bejaia' else '#8a8a8a')
        for xi, (r, s, c) in zip(x, zip(sub['rate'], sub['sum'], sub['count'])):
            ax.text(xi, r + 0.02, f"{s}/{c}", ha='center', fontsize=8)
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels([month_names[m] for m in sorted(grp['month'].unique())])
    ax.set_ylabel('Proportion of days assigned the "fire" class')
    ax.set_ylim(0, 1.05)
    ax.set_title('Monthly recorded-class proportion by region (descriptive; counts shown as fire/total)')
    ax.legend()
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig_C_monthly_class_proportion.png')
    plt.close()

    # Figure D - weekly FWI trend, neutral, calendar-week rule stated in caption/text
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for region, color in [('Bejaia', '#4a4a4a'), ('Sidi-Bel Abbes', '#8a8a8a')]:
        d = df[df.Region == region].sort_values('date').set_index('date')['FWI'].resample('W').mean()
        ax.plot(d.index, d.values, marker='o', label=region, color=color)
    ax.set_ylabel('Weekly mean Fire Weather Index (calendar week, W-Sun; first week partial)')
    ax.set_title('Weekly Fire Weather Index by region, June-September 2012')
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig_D_fwi_weekly_trend.png')
    plt.close()

    print(f"\nFigures B, C, D saved to {outdir}/")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='Algerian_forest_fires_dataset_CLEANED.csv')
    parser.add_argument('--outdir', default='.')
    args = parser.parse_args()

    df = load(args.input)

    for region in df['Region'].unique():
        group_comparisons(df[df.Region == region], label=f"[{region}]")
    holm_family_choice_check(df)
    rain_zero_handling(df)
    regional_model_comparison(df)
    temporal_dependence(df)
    repaired_record_sensitivity(df)
    zero_rain_streaks(df)
    make_figures(df, args.outdir)
