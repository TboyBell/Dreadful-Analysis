"""
DAM140 - Phase 3 (Revised): Research Questions, EDA and Statistical Analysis
Audit-corrected version.

This single script reproduces every numerical result, statistical test,
effect size, correction, sensitivity check and figure referenced in the
Phase 3 revised write-up. It reads the cleaned dataset produced by
clean_forest_fires.py.

Aggregation rule used throughout for "weekly" figures: calendar weeks
ending Sunday (pandas .resample('W'), i.e. W-SUN), applied separately
within each region's time-ordered series. This is stated explicitly
because the audit required the exact aggregation method to be defined.

No random sampling is used anywhere in this script (all effect sizes and
intervals below have closed-form calculations), so no random seed is
required for reproducibility.
"""

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.proportion import proportion_confint
from statsmodels.tsa.stattools import acf
import statsmodels.api as sm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

CLEANED_PATH = "Algerian_forest_fires_dataset_CLEANED.csv"
pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)


def load():
    df = pd.read_csv(CLEANED_PATH, parse_dates=['date'])
    df['fire_flag'] = (df.Classes == 'fire').astype(int)
    return df


# ---------------------------------------------------------------------------
# Effect size helpers
# ---------------------------------------------------------------------------

def cliffs_delta(x, y):
    """
    Exact Cliff's delta via pairwise comparison (safe at this sample size:
    138 x 106 = 14,628 pairs). delta in [-1, 1]; positive means x tends to
    be larger than y. Rank-biserial correlation for two independent
    samples is numerically identical to Cliff's delta.
    """
    x = np.asarray(x); y = np.asarray(y)
    gt = 0; lt = 0
    for xi in x:
        gt += np.sum(xi > y)
        lt += np.sum(xi < y)
    n = len(x) * len(y)
    return (gt - lt) / n


def cramers_v(chi2, n, r, c):
    return np.sqrt(chi2 / (n * (min(r, c) - 1)))


def wilson_ci(count, nobs, alpha=0.05):
    return proportion_confint(count, nobs, alpha=alpha, method='wilson')


# ---------------------------------------------------------------------------
# 1. Group comparisons: Temperature, RH, Ws, Rain (fire vs not fire)
# ---------------------------------------------------------------------------

def group_comparisons(df, label=""):
    print(f"\n--- Group comparisons (fire vs not fire) {label} ---")
    cols = ['Temperature', 'RH', 'Ws', 'Rain']
    results = []
    for col in cols:
        fire = df[df.Classes == 'fire'][col]
        notfire = df[df.Classes == 'not fire'][col]
        u, p = stats.mannwhitneyu(fire, notfire, alternative='two-sided')
        delta = cliffs_delta(fire.values, notfire.values)
        results.append({
            'variable': col,
            'median_fire': fire.median(), 'iqr_fire': (fire.quantile(.25), fire.quantile(.75)),
            'median_notfire': notfire.median(), 'iqr_notfire': (notfire.quantile(.25), notfire.quantile(.75)),
            'U': u, 'p_raw': p, 'cliffs_delta': delta
        })
    res_df = pd.DataFrame(results)
    # Holm correction across these 4 exploratory tests
    reject, p_holm, _, _ = multipletests(res_df['p_raw'], method='holm', alpha=0.05)
    res_df['p_holm'] = p_holm
    res_df['significant_after_holm'] = reject
    print(res_df.to_string(index=False))
    return res_df


def rain_zero_handling(df, label=""):
    print(f"\n--- Rain zero-value handling {label} ---")
    for cls in ['fire', 'not fire']:
        sub = df[df.Classes == cls]['Rain']
        zero_prop = (sub == 0).mean()
        nonzero = sub[sub > 0]
        print(f"{cls:10s}: zero-rain proportion={zero_prop:.3f}  "
              f"(n={len(sub)}); non-zero median={nonzero.median() if len(nonzero) else float('nan'):.2f}, "
              f"IQR=({nonzero.quantile(.25) if len(nonzero) else float('nan'):.2f},"
              f"{nonzero.quantile(.75) if len(nonzero) else float('nan'):.2f}), n_nonzero={len(nonzero)}")


def comparisons_by_region_and_month(df):
    print("\n--- Group comparisons repeated by region (confounding check) ---")
    for region in df['Region'].unique():
        group_comparisons(df[df.Region == region], label=f"[{region}]")

    print("\n--- Fire vs not-fire median Temperature/RH by month (confounding check) ---")
    print(df.groupby(['month', 'Classes'])[['Temperature', 'RH']].median().round(1))


# ---------------------------------------------------------------------------
# 2. Regional association
# ---------------------------------------------------------------------------

def regional_association(df):
    print("\n--- Regional association ---")
    ct = pd.crosstab(df['Region'], df['Classes'])
    pct = pd.crosstab(df['Region'], df['Classes'], normalize='index')
    print("Counts:\n", ct)
    print("Row percentages:\n", (pct * 100).round(1))

    chi2, p, dof, exp = stats.chi2_contingency(ct)
    n = ct.values.sum()
    v = cramers_v(chi2, n, *ct.shape)
    print(f"chi2={chi2:.3f}, p={p:.4f}, dof={dof}, Cramer's V={v:.3f}")
    print("Interpretation: Cramer's V in this range is conventionally a 'small' "
          "association (Cohen, 1988 thresholds: ~0.1 small, ~0.3 medium, ~0.5 large "
          "for df=1). This describes an association observed in the June-Sept 2012 "
          "sample only; it is not evidence that region causes fire risk.")

    # Does region remain associated with fire after adjusting for weather?
    X = df[['Temperature', 'RH']].copy()
    X['region_sidi'] = (df['Region'] == 'Sidi-Bel Abbes').astype(int)
    X = sm.add_constant(X)
    y = df['fire_flag']
    model = sm.Logit(y, X).fit(disp=0)
    print("\nLogistic regression: fire_flag ~ Temperature + RH + region_sidi")
    print(model.summary2().tables[1])
    return {'chi2': chi2, 'p': p, 'cramers_v': v, 'logit_model': model}


# ---------------------------------------------------------------------------
# 3. Temporal dependence
# ---------------------------------------------------------------------------

def temporal_dependence(df):
    print("\n--- Temporal dependence (autocorrelation within each region's time-ordered series) ---")
    print("Note: DMC and DC are defined recursively in the Canadian FWI system "
          "(each day's value updates the previous day's value using that day's "
          "weather; Van Wagner, 1987), so material autocorrelation in these codes "
          "is expected by construction, not an anomaly.")
    for region in df['Region'].unique():
        sub = df[df.Region == region].sort_values('date')
        print(f"\n{region}:")
        for col in ['Temperature', 'DC', 'FFMC']:
            vals = acf(sub[col], nlags=7, fft=False)
            print(f"  {col:12s} ACF lag1-7: " + ", ".join(f"{v:.2f}" for v in vals[1:]))
    print("\nImplication: because consecutive days within a region are not "
          "independent, the Mann-Whitney tests above (which assume independent "
          "samples) likely understate the true p-values (i.e. are somewhat "
          "optimistic/anti-conservative). Conclusions are restricted to the "
          "observed June-Sept 2012 window and should not be read as i.i.d. "
          "sampling from a larger population.")


# ---------------------------------------------------------------------------
# 4. Correlation and feature dependency
# ---------------------------------------------------------------------------

def correlation_analysis(df):
    print("\n--- Correlation and feature dependency (corrected) ---")
    num_cols = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']
    pearson = df[num_cols].corr(method='pearson')
    spearman = df[num_cols].corr(method='spearman')

    print("Precise DMC-DC-BUI trio (Pearson, 6dp):")
    print(df[['DMC', 'DC', 'BUI']].corr().round(6))
    print("\nCorrected statement: DMC-DC r=0.8754 (does NOT exceed 0.88); "
          "DMC-BUI r=0.9822 and DC-BUI r=0.9417 DO exceed 0.88. All three are "
          "strong, and the relationship is partly structural: BUI is calculated "
          "directly FROM DMC and DC by a fixed formula in the Canadian FWI "
          "system (Van Wagner, 1987), so part of this correlation is by "
          "mathematical construction, not an empirical pattern to 'discover'.")

    print("\nPearson vs Spearman (selected pairs):")
    for a, b in [('DMC', 'DC'), ('DC', 'BUI'), ('Temperature', 'FFMC')]:
        print(f"  {a}-{b}: Pearson={pearson.loc[a,b]:.3f}, Spearman={spearman.loc[a,b]:.3f}")

    print("\nUnivariate association of each variable with the class label "
          "(point-biserial correlation - NOT model-based feature importance):")
    df2 = df.copy()
    assoc = df2[num_cols + ['fire_flag']].corr()['fire_flag'].drop('fire_flag').sort_values(ascending=False)
    print(assoc.round(3))
    print("\nNote: predictors are NOT being removed at this stage on the basis of "
          "pairwise correlation alone. Multicollinearity and redundancy will be "
          "assessed in the context of the specific model chosen in the modelling "
          "phase (e.g. via VIF or regularisation), not decided here.")
    return pearson, spearman


# ---------------------------------------------------------------------------
# 5. Repaired-record sensitivity
# ---------------------------------------------------------------------------

def repaired_record_sensitivity(df):
    print("\n--- Repaired-record sensitivity analysis ---")
    df_excl = df[~df['record_repaired']].copy()
    print(f"n with repaired record: {len(df)}; n excluding it: {len(df_excl)}")

    print("\nMann-Whitney U p-values, with vs without the repaired record:")
    for col in ['Temperature', 'RH', 'Ws', 'Rain']:
        f1, nf1 = df[df.Classes == 'fire'][col], df[df.Classes == 'not fire'][col]
        f2, nf2 = df_excl[df_excl.Classes == 'fire'][col], df_excl[df_excl.Classes == 'not fire'][col]
        _, p1 = stats.mannwhitneyu(f1, nf1)
        _, p2 = stats.mannwhitneyu(f2, nf2)
        print(f"  {col:12s} with={p1:.2e}   without={p2:.2e}")

    ct1 = pd.crosstab(df['Region'], df['Classes'])
    ct2 = pd.crosstab(df_excl['Region'], df_excl['Classes'])
    chi2_1, p1, _, _ = stats.chi2_contingency(ct1)
    chi2_2, p2, _, _ = stats.chi2_contingency(ct2)
    print(f"\nRegion chi-square: with chi2={chi2_1:.3f},p={p1:.4f}  "
          f"without chi2={chi2_2:.3f},p={p2:.4f}")

    dmc_dc_1 = df[['DMC', 'DC']].corr().iloc[0, 1]
    dmc_dc_2 = df_excl[['DMC', 'DC']].corr().iloc[0, 1]
    print(f"\nDMC-DC correlation: with={dmc_dc_1:.4f}  without={dmc_dc_2:.4f}")
    print("Conclusion: removing the single reconstructed record changes no "
          "result at a level that would alter any interpretation above.")


# ---------------------------------------------------------------------------
# 6. Figures (revised)
# ---------------------------------------------------------------------------

def make_figures(df):
    plt.rcParams.update({'font.size': 11, 'figure.dpi': 150})

    # Fig A: class balance (unchanged from Phase 3 draft, kept for reference)
    fig, ax = plt.subplots(figsize=(5, 4))
    counts = df['Classes'].value_counts()
    ax.bar(counts.index, counts.values, color=['#8a8a8a', '#4a4a4a'])
    ax.set_title('Record counts by class label (n=244)')
    ax.set_ylabel('Number of records')
    plt.tight_layout()
    plt.savefig('fig_A_class_balance.png')
    plt.close()

    # Fig B: raw weather variables by class, full names + units, with medians marked
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
    fig.suptitle('Meteorological variables by recorded class (June-Sept 2012)')
    plt.tight_layout()
    plt.savefig('fig_B_weather_by_class.png')
    plt.close()

    # Fig C: fire rate by month and region WITH Wilson 95% CIs
    grp = df.groupby(['month', 'Region'])['fire_flag'].agg(['sum', 'count']).reset_index()
    grp['rate'] = grp['sum'] / grp['count']
    ci = grp.apply(lambda r: wilson_ci(r['sum'], r['count']), axis=1)
    grp['ci_low'] = ci.apply(lambda x: x[0])
    grp['ci_high'] = ci.apply(lambda x: x[1])

    month_names = {6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep'}
    fig, ax = plt.subplots(figsize=(8, 4.5))
    width = 0.35
    for i, region in enumerate(['Bejaia', 'Sidi-Bel Abbes']):
        sub = grp[grp.Region == region].sort_values('month')
        x = np.arange(len(sub)) + (i - 0.5) * width
        yerr = [sub['rate'] - sub['ci_low'], sub['ci_high'] - sub['rate']]
        ax.bar(x, sub['rate'], width, label=region,
               color='#4a4a4a' if region == 'Bejaia' else '#8a8a8a',
               yerr=yerr, capsize=4)
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels([month_names[m] for m in sorted(grp['month'].unique())])
    ax.set_ylabel('Proportion of days classed "fire" (95% Wilson CI)')
    ax.set_title('Monthly fire-day proportion by region, with 95% confidence intervals')
    ax.legend()
    plt.tight_layout()
    plt.savefig('fig_C_fire_rate_region_month_CI.png')
    plt.close()

    # Fig D: FWI seasonal trend, neutral title, calendar-week aggregation (defined),
    # both regions shown but NOT visually implying one continuous series across regions
    # (they are two separately-computed lines, each internally consistent by region,
    # which is an accepted way to compare two independent time series side by side -
    # the issue flagged was joining DMC/DC/BUI of DIFFERENT VARIABLES incorrectly,
    # addressed in Fig E below).
    fig, ax = plt.subplots(figsize=(9, 4.5))
    for region, color in [('Bejaia', '#4a4a4a'), ('Sidi-Bel Abbes', '#8a8a8a')]:
        d = df[df.Region == region].sort_values('date').set_index('date')['FWI'].resample('W').mean()
        ax.plot(d.index, d.values, marker='o', label=region, color=color)
    ax.set_ylabel('Weekly mean Fire Weather Index (calendar week, W-Sun)')
    ax.set_title('Observed late-August Fire Weather Index peak, by region')
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig('fig_D_fwi_seasonal_trend_neutral.png')
    plt.close()

    # Fig E (REPLACEMENT for old chart6): DMC/DC/BUI standardised, one subplot per region
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5), sharey=True)
    for ax, region in zip(axes, ['Bejaia', 'Sidi-Bel Abbes']):
        sub = df[df.Region == region].sort_values('date')
        for col, color in zip(['DMC', 'DC', 'BUI'], ['#4a4a4a', '#8a8a8a', '#c2c2c2']):
            z = (sub[col] - sub[col].mean()) / sub[col].std()
            ax.plot(sub['date'], z, label=col, color=color)
        ax.set_title(region)
        ax.set_xlabel('Date')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
    axes[0].set_ylabel('Standardised value (z-score)')
    axes[0].legend()
    fig.suptitle('DMC, DC and BUI move together within each region (standardised, shown separately per region)')
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig('fig_E_multicollinearity_by_region.png')
    plt.close()

    print("\nAll revised figures saved: fig_A .. fig_E")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    df = load()

    group_comparisons(df)
    rain_zero_handling(df)
    comparisons_by_region_and_month(df)
    regional_association(df)
    temporal_dependence(df)
    correlation_analysis(df)
    repaired_record_sensitivity(df)
    make_figures(df)
