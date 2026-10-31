# Algerian Forest Fires — Data Analytics & Visualisation

An end-to-end Python data analytics project demonstrating **data cleaning, transformation, exploratory data analysis, statistical investigation, visualisation, reproducibility, data lineage and scalable analytics architecture**.

The project was completed as part of the DAM140 Big Data Analytics and Visualisation module using the Algerian Forest Fires dataset.

The technical focus of the project was building a controlled analytical workflow that transforms raw data into validated analytical outputs while preserving the ability to reproduce and audit each stage.

---

# Technical Architecture

The project follows a staged analytical pipeline:

```text
Raw Dataset
     │
     ▼
Data Inspection
     │
     ▼
Python Cleaning Pipeline
     │
     ▼
Cleaned Dataset
     │
     ▼
Exploratory Data Analysis
     │
     ├────────► Statistical Analysis
     │
     ├────────► Correlation Analysis
     │
     ├────────► Trend Analysis
     │
     └────────► Comparative Analysis
     │
     ▼
Visualisations
     │
     ▼
Analytical Findings
     │
     ▼
Evaluation
     │
     ▼
Scalable Architecture Considerations
```

The project deliberately separated these stages instead of performing transformations manually during analysis.

This creates a more reproducible analytics workflow.

---

# Technology Stack

## Python

Python was used as the primary analytical programming language.

Python scripts were created for separate stages of the workflow rather than performing the entire analysis interactively.

Key project scripts include:

```text
clean_forest_fires.py
phase3_frozen.py
```

This separation provides clearer responsibility between:

```text
Data Preparation
      ↓
Analytical Processing
      ↓
Visualisation
```

---

## Pandas

Pandas was used for structured tabular data processing.

Typical operations within the analytical workflow involved:

- loading CSV datasets
- inspecting columns and data types
- cleaning values
- transforming columns
- filtering records
- grouping observations
- calculating aggregate statistics
- preparing data for visualisation
- comparing categories
- exporting cleaned datasets

Conceptually:

```python
Raw CSV
   ↓
pandas.DataFrame
   ↓
Cleaning
   ↓
Transformation
   ↓
Validation
   ↓
Analysis-ready DataFrame
   ↓
Clean CSV
```

Using a DataFrame-based workflow allowed transformations to be expressed programmatically and reproduced.

---

## NumPy

NumPy supported numerical operations required during data preparation and analytical processing.

Together, Pandas and NumPy provide the underlying tabular and numerical processing capabilities used throughout the workflow.

---

## Matplotlib

Matplotlib was used to create analytical visualisations.

The frozen analytical outputs include visualisations examining areas such as:

```text
Weather Conditions by Fire Classification

Monthly Fire / Non-Fire Class Proportions

Weekly Fire Weather Index Trends
```

Visualisation was treated as part of the analytical process rather than simply presentation.

Graphs were used to expose patterns and support interpretation of the underlying data.

---

# Data Cleaning Pipeline

A dedicated Python cleaning pipeline was created:

```text
clean_forest_fires.py
```

The workflow follows the principle:

```text
Original Dataset
      │
      │ never modified directly
      ▼
Cleaning Script
      │
      ▼
Validated Clean Dataset
```

The original data was therefore preserved separately from transformed data.

The resulting cleaned dataset was stored as:

```text
Algerian_forest_fires_dataset_CLEANED.csv
```

This separation is important because it creates traceability between the source data and analytical dataset.

---

# Data Quality

Before analysis, the dataset required preparation to ensure that the analytical code was operating against a consistent structure.

The cleaning stage focused on areas such as:

- column consistency
- data type preparation
- malformed or inconsistent values
- categorical values
- missing or unsuitable observations
- structural inconsistencies
- analysis-ready formatting

Instead of silently changing values within the exploratory analysis, transformations were placed into a repeatable script.

This supports:

```text
Repeatability
Auditability
Consistency
Traceability
```

---

# Exploratory Data Analysis

Following cleaning, the dataset was analysed through a dedicated EDA stage.

The final frozen analysis is represented by:

```text
phase3_frozen.py
```

The analysis investigated relationships between forest-fire classifications and environmental variables.

Areas examined included:

- fire versus non-fire observations
- meteorological characteristics
- monthly patterns
- seasonal behaviour
- Fire Weather Index behaviour
- correlations between variables
- potential multicollinearity
- differences between groups

---

# Fire Weather Index Analysis

The project included analysis of **Fire Weather Index (FWI)** behaviour.

Rather than simply reporting individual values, time-based analysis was used to examine how the index changed across the dataset.

A frozen project output includes:

```text
fig_D_fwi_weekly_trend.png
```

This demonstrates the use of:

```text
Raw observations
      ↓
Time grouping
      ↓
Aggregation
      ↓
Trend analysis
      ↓
Visual interpretation
```

This type of analytical transformation is commonly required when converting low-level observations into decision-useful information.

---

# Categorical Comparison

The analysis compared observations classified as fire and non-fire.

This required grouping records according to classification and examining whether environmental characteristics differed between groups.

A frozen output includes:

```text
fig_B_weather_by_class.png
```

This demonstrates analytical techniques including:

- category-based grouping
- distribution comparison
- descriptive statistics
- visual comparison

---

# Temporal Analysis

The project also investigated how fire classifications changed across time.

One frozen visualisation is:

```text
fig_C_monthly_class_proportion.png
```

Instead of using raw counts alone, class proportions allow patterns to be compared across periods with different numbers of observations.

Conceptually:

```text
Observations
     ↓
Extract Month
     ↓
Group by Month + Class
     ↓
Calculate Class Proportion
     ↓
Visualise Seasonal Pattern
```

---

# Correlation & Multicollinearity

The exploratory work also investigated correlation between numerical variables.

Correlation analysis helps identify variables that move together and provides insight into the internal structure of a dataset.

Earlier exploratory artefacts included correlation and multicollinearity analysis before the final frozen analytical subset was selected.

This demonstrates understanding that highly correlated variables may contain overlapping information and can affect later analytical or predictive approaches.

---

# Reproducibility

One of the strongest technical aspects of the project is the controlled handling of analytical outputs.

Rather than continuously overwriting previous analysis, project stages were **frozen** after review.

The repository contains separate areas for:

```text
Original Data
Frozen Cleaning Pipeline
Frozen EDA
References
Audit Records
Superseded Files
```

This creates a clear distinction between:

```text
Source
   ↓
Current Approved Processing
   ↓
Current Approved Outputs
```

and previous analytical iterations.

---

# Analytical Version Control

Previous analysis was not treated as current evidence once superseded.

Earlier files were moved into:

```text
99_Superseded_File_List/
└── Archive_Do_Not_Use/
```

Examples include previous:

- correlation visualisations
- seasonal trend plots
- multicollinearity analysis
- EDA scripts
- revised analytical scripts

This approach demonstrates an important analytical engineering principle:

> an analysis should make it clear which artefacts represent the authoritative result.

---

# Manifests

The project contains manifest files including:

```text
MASTER_MANIFEST.csv
PHASE2_MANIFEST.csv
```

These provide an inventory of project artefacts and help establish which files belong to a particular frozen analytical release.

This introduces concepts normally associated with controlled data and software pipelines:

- artefact management
- provenance
- release management
- traceability

---

# SHA-256 Checksums

The frozen project also contains:

```text
CHECKSUMS_SHA256.txt
```

SHA-256 hashes provide a way to verify whether frozen artefacts have changed.

Conceptually:

```text
File
 │
 ▼
SHA-256
 │
 ▼
Unique Hash
```

If the file changes:

```text
Original file → abc123...
Modified file → 91fd72...
```

the checksum changes.

This provides additional integrity verification for frozen analytical artefacts.

---

# Audit Records

The project includes explicit audit documentation:

```text
05_Audit_Records/
├── AUDIT_STATUS.md
├── PHASE2_AUDIT_DECISION.txt
└── PHASE3_AUDIT_DECISION.txt
```

These records document decisions around which analytical artefacts were approved and frozen.

This goes beyond producing graphs and demonstrates awareness of **analytical governance and reproducibility**.

---

# Project Structure

A simplified representation of the frozen project structure is:

```text
DAM140_Phases_1_to_3_Frozen/
│
├── 00_Assessment_Documents/
│
├── 01_Original_Data/
│   ├── algerian_forest_fires_dataset.zip
│   └── ORIGINAL_DATA_README.md
│
├── 02_Phase_2_Cleaning_Frozen/
│   ├── Algerian_forest_fires_dataset_CLEANED.csv
│   ├── clean_forest_fires.py
│   ├── PHASE2_FROZEN_README.md
│   └── PHASE2_MANIFEST.csv
│
├── 03_Phase_3_EDA_Frozen/
│   ├── phase3_frozen.py
│   ├── fig_B_weather_by_class.png
│   ├── fig_C_monthly_class_proportion.png
│   ├── fig_D_fwi_weekly_trend.png
│   ├── PHASE3_FROZEN_README.md
│   ├── PHASE3_FROZEN_SUMMARY.md
│   └── requirements.txt
│
├── 04_References/
│
├── 05_Audit_Records/
│
├── 99_Superseded_File_List/
│
├── CHECKSUMS_SHA256.txt
├── MASTER_MANIFEST.csv
└── RELEASE_NOTES.md
```

This structure itself demonstrates an attempt to treat analytics as a controlled technical workflow rather than a collection of disconnected notebooks or graphs.

---

# Analytical Pipeline Design

A useful way of viewing the project is:

```text
                DATA PIPELINE
                     │
                     ▼
┌─────────────────────────────┐
│        RAW DATA             │
│ Immutable source dataset    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      DATA CLEANING          │
│ clean_forest_fires.py       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      CLEAN DATASET          │
│ Controlled analytical data │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│            EDA              │
│ phase3_frozen.py            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      VISUALISATIONS         │
│ Trends / comparisons        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     ANALYTICAL FINDINGS     │
└─────────────────────────────┘
```

---

# Scalable Analytics Architecture

The later stage of the project also considered how the workflow would need to change if the dataset increased substantially in volume.

A local architecture based around:

```text
CSV
 ↓
Python
 ↓
Pandas
 ↓
Local Processing
```

is appropriate for relatively small analytical datasets.

At larger scale, the architecture would need to separate ingestion, storage and compute.

Conceptually:

```text
Data Sources
     │
     ▼
Data Ingestion
     │
     ▼
Scalable Storage
     │
     ▼
Distributed Processing
     │
     ▼
Curated Analytical Data
     │
     ▼
Analytics / Visualisation
```

The project therefore considered not only how analysis works locally but the architectural implications of performing similar processing against larger datasets.

---

# Privacy, Governance & Legislation

The project also considered the broader responsibilities involved in large-scale data processing.

This included discussion of:

- privacy
- data protection
- responsible processing
- data governance
- security controls
- legal obligations
- risk mitigation

This demonstrates awareness that technical data solutions must account for both analytical requirements and governance constraints.

---

# Technical Competencies Demonstrated

## Python

- scripting analytical workflows
- separating processing stages
- repeatable data transformation

## Pandas

- DataFrame manipulation
- filtering
- grouping
- aggregation
- data cleaning
- categorical analysis
- CSV processing

## NumPy

- numerical data processing
- analytical calculations

## Matplotlib

- programmatic data visualisation
- trend plots
- comparative visualisation
- analytical communication

## Data Cleaning

- raw-to-clean transformation
- quality checking
- standardisation
- reproducible processing

## Exploratory Data Analysis

- descriptive analysis
- correlation analysis
- temporal analysis
- categorical comparison
- trend identification
- multicollinearity investigation

## Analytical Engineering

- reproducible pipelines
- separation of raw and processed data
- frozen analytical releases
- file manifests
- audit records
- SHA-256 integrity checks
- superseded artefact management

## Data Architecture

- analytical pipeline design
- scalable storage concepts
- distributed processing concepts
- separation of ingestion, storage, compute and analytics

## Data Governance

- lineage
- traceability
- integrity
- privacy
- data protection considerations

---

# What This Project Demonstrates

The project demonstrates more than the ability to create visualisations.

It demonstrates the complete process:

```text
Can I understand an unfamiliar dataset?
                ↓
Can I identify data-quality problems?
                ↓
Can I clean those problems programmatically?
                ↓
Can somebody reproduce that transformation?
                ↓
Can I analyse the resulting dataset?
                ↓
Can I identify meaningful patterns?
                ↓
Can I communicate those patterns visually?
                ↓
Can I preserve which results are authoritative?
                ↓
Can I demonstrate data lineage?
                ↓
Can I consider how the solution scales?
```
