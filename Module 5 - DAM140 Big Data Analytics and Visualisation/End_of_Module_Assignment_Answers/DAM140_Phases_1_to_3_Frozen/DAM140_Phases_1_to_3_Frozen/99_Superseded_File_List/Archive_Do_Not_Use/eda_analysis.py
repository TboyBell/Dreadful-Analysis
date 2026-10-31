"""
DAM140 - Phase 3 Part B: Exploratory Data Analysis
Runs on the cleaned dataset produced by clean_forest_fires.py

Sections:
    1. Descriptive statistics (overall, by class, by region)
    2. Statistical tests (Mann-Whitney U for weather vars; chi-square for region x class)
    3. Correlation / multicollinearity analysis
    4. Temporal pattern analysis
    5. Outlier / unusual-observation identification
    6. Visualisations (saved as PNG files)
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

CLEANED_PATH = "Algerian_forest_fires_dataset_CLEANED.csv"


def load():
    df = pd.read_csv(CLEANED_PATH, parse_dates=['date'])
    df['fire_flag'] = (df.Classes == 'fire').astype(int)
    return df


def descriptive_stats(df):
    num_cols = ['Temperature','RH','Ws','Rain','FFMC','DMC','DC','ISI','BUI','FWI']
    print("By Classes:\n", df.groupby('Classes')[num_cols].mean().round(2))
    print("\nBy Region:\n", df.groupby('Region')[num_cols].mean().round(2))
    print("\nFire rate by region:\n", pd.crosstab(df['Region'], df['Classes'], normalize='index').round(3))


def statistical_tests(df):
    print("\nMann-Whitney U (fire vs not fire):")
    for col in ['Temperature','RH','Ws','Rain']:
        fire = df[df.Classes=='fire'][col]
        notfire = df[df.Classes=='not fire'][col]
        u, p = stats.mannwhitneyu(fire, notfire, alternative='two-sided')
        print(f"  {col:12s} U={u:9.1f}  p={p:.2e}")

    ct = pd.crosstab(df['Region'], df['Classes'])
    chi2, p, dof, exp = stats.chi2_contingency(ct)
    print(f"\nChi-square Region x Classes: chi2={chi2:.3f}, p={p:.4f}, dof={dof}")


def correlation_analysis(df):
    num_cols = ['Temperature','RH','Ws','Rain','FFMC','DMC','DC','ISI','BUI','FWI']
    corr = df[num_cols].corr()
    print("\nCorrelation with fire_flag:\n",
          df[num_cols+['fire_flag']].corr()['fire_flag'].sort_values(ascending=False).round(3))
    return corr


def temporal_patterns(df):
    print("\nFire rate by month:\n", df.groupby('month')['fire_flag'].mean().round(3))
    print("\nFire rate by month x region:\n", df.groupby(['month','Region'])['fire_flag'].mean().round(3))


def outlier_check(df):
    for col in ['DC','BUI','FWI','Rain']:
        z = (df[col]-df[col].mean())/df[col].std()
        top = df.loc[z.abs().sort_values(ascending=False).index[:3], ['date','Region','Classes',col]]
        print(f"\nTop |z| for {col}:\n{top}")


if __name__ == "__main__":
    df = load()
    descriptive_stats(df)
    statistical_tests(df)
    correlation_analysis(df)
    temporal_patterns(df)
    outlier_check(df)
