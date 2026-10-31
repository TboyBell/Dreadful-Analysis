"""
DAM140 - Big Data Analytics and Visualization
Algerian Forest Fires dataset - inspection and cleaning pipeline

Revision note (post audit-review):
    - Column names are now derived dynamically from the file's own header
      row (stripped of whitespace) rather than substituted from a
      hardcoded constant. An assertion checks the result matches the
      documented attribute set, so a silently different file would fail
      loudly rather than being mis-labelled.
    - The one repaired record is now explicitly flagged in the output
      (see 'record_repaired' column) and described as the most plausible
      reconstruction rather than an unquestionable fact.
    - File encoding changed from ASCII to UTF-8 for portability.
    - Key invariants are now enforced with assertions, not just printed.
    - Paths are CLI-configurable (with the original values as defaults).

This script is organised into clearly separated stages:
    1. Raw file loading and inspection
    2. Structural parsing (splitting the two embedded region blocks)
    3. Row-level repair (malformed record)
    4. Type coercion and whitespace/label standardisation
    5. Validation (duplicates, missing values, dtypes, ranges) with assertions
    6. Export of the cleaned dataset

Run with: python3 clean_forest_fires.py [--raw-path PATH] [--output-path PATH]
"""

import re
import argparse
import pandas as pd
import numpy as np

DEFAULT_RAW_PATH = "fires_data/Algerian_forest_fires_dataset_UPDATE.csv"
DEFAULT_OUTPUT_PATH = "Algerian_forest_fires_dataset_CLEANED.csv"

# Used only to VALIDATE that the header actually found in the file matches
# the documented attribute set - not used to name the columns directly.
EXPECTED_COLUMNS = [
    "day", "month", "year", "Temperature", "RH", "Ws", "Rain",
    "FFMC", "DMC", "DC", "ISI", "BUI", "FWI", "Classes"
]

# ---------------------------------------------------------------------------
# STAGE 1: Raw inspection (read-only, no modification)
# ---------------------------------------------------------------------------

def inspect_raw_file(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw_lines = f.readlines()

    print(f"Total raw lines in file: {len(raw_lines)}")

    region_marker_lines = [i for i, l in enumerate(raw_lines)
                            if "Region Dataset" in l]
    blank_lines = [i for i, l in enumerate(raw_lines) if l.strip() == ""]
    header_lines = [i for i, l in enumerate(raw_lines)
                     if l.strip().startswith("day,month,year")]

    print(f"Region title rows found at line indices: {region_marker_lines}")
    print(f"Blank separator rows at line indices: {blank_lines}")
    print(f"Embedded header rows at line indices: {header_lines}")

    field_counts = {}
    for l in raw_lines:
        n = len(l.strip().split(",")) if l.strip() else 0
        field_counts[n] = field_counts.get(n, 0) + 1
    print(f"Field-count distribution across all raw lines: {field_counts}")

    # Derive the actual column names from the file itself, rather than
    # assuming they match a hardcoded list. Every embedded header row is
    # checked, since the two regional blocks each carry their own copy.
    derived_columns = None
    for i in header_lines:
        cols = [c.strip() for c in raw_lines[i].strip().split(",")]
        if derived_columns is None:
            derived_columns = cols
        elif cols != derived_columns:
            raise ValueError(
                f"Header at line {i+1} does not match header at an earlier "
                f"region block ({cols} vs {derived_columns}) - the file's "
                f"structure is not what this script assumes."
            )

    assert derived_columns == EXPECTED_COLUMNS, (
        f"Header derived from file ({derived_columns}) does not match the "
        f"documented Algerian Forest Fires attribute set ({EXPECTED_COLUMNS}). "
        f"Stopping rather than silently mislabelling columns."
    )
    print(f"Header verified against documented attribute set: {derived_columns}")

    return raw_lines, derived_columns


# ---------------------------------------------------------------------------
# STAGE 2: Structural parsing - split into region blocks and data rows
# ---------------------------------------------------------------------------

def parse_regions(raw_lines, columns):
    """
    Walks the raw file line by line. Any line containing 'Region Dataset'
    starts a new region block; the region name is taken from that line.
    Header rows and blank rows are skipped. Everything else is treated
    as a data row and tagged with the current region.
    """
    records = []
    current_region = None
    malformed = []
    repaired_line_indices = []

    for idx, line in enumerate(raw_lines):
        stripped = line.strip()

        if stripped == "":
            continue
        if "Region Dataset" in stripped:
            current_region = stripped.replace("Region Dataset", "").strip()
            continue
        if stripped.startswith("day,month,year"):
            continue  # embedded header row, already verified in Stage 1

        parts = [p for p in stripped.split(",")]
        was_fixed = False

        if len(parts) != len(columns):
            parts, was_fixed = attempt_repair(parts, idx, line, columns)
            if not was_fixed:
                malformed.append((idx, current_region, stripped))
                continue
            repaired_line_indices.append(idx)

        record = dict(zip(columns, parts))
        record["Region"] = current_region
        record["record_repaired"] = was_fixed
        record["_raw_line_index"] = idx
        records.append(record)

    return pd.DataFrame(records), malformed, repaired_line_indices


# ---------------------------------------------------------------------------
# STAGE 3: Row-level repair
# ---------------------------------------------------------------------------

NUMERIC_PAIR_PATTERN = re.compile(r"^-?\d+\.?\d*\s+-?\d+\.?\d*$")

def attempt_repair(parts, idx, original_line, columns):
    """
    Handles the one known malformed record in this dataset: a missing
    comma between two numeric fields (e.g. '14.6 9' instead of '14.6,9'),
    which leaves the row one field short.

    Strategy: if the row is exactly one field short of the expected
    column count, search for a single field that actually contains two
    whitespace-separated numbers, and split it into two fields at that
    point. This is a general, auditable rule (not a row-specific patch),
    so it would also catch any other instance of the same fault
    elsewhere in the file - none were found besides the one below.

    IMPORTANT: this is a reconstruction, not a verified correction - the
    original comma is genuinely missing from the source file and cannot
    be recovered with certainty. The split is the most plausible reading
    given (a) column order and (b) that both resulting values fall
    within the normal range observed elsewhere in the dataset for those
    two columns, but it is flagged via 'record_repaired=True' in the
    output so it can be excluded or scrutinised in later analysis if
    that plausibility is doubted.
    """
    if len(parts) != len(columns) - 1:
        return parts, False

    for i, field in enumerate(parts):
        if NUMERIC_PAIR_PATTERN.match(field.strip()):
            a, b = field.strip().split()
            fixed = parts[:i] + [a, b] + parts[i + 1:]
            print(f"[REPAIR - most plausible reconstruction, not certain fact] "
                  f"Raw line {idx + 1}: split field {i} "
                  f"('{field.strip()}' -> '{a}', '{b}') | original: {original_line.strip()}")
            return fixed, True

    return parts, False


# ---------------------------------------------------------------------------
# STAGE 4: Type coercion and standardisation
# ---------------------------------------------------------------------------

def clean_types(df, columns):
    df = df.copy()

    # Strip whitespace from every string cell. Column names themselves are
    # already exact, since Stage 1 derived + verified them from the file.
    for col in columns + ["Region"]:
        df[col] = df[col].astype(str).str.strip()

    int_cols = ["day", "month", "year", "Temperature", "RH", "Ws"]
    float_cols = ["Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]

    for col in int_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    for col in float_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)

    # Standardise the target label: lowercase, whitespace-stripped,
    # collapsed internal spacing.
    df["Classes"] = (
        df["Classes"].str.strip().str.lower()
        .str.replace(r"\s+", " ", regex=True)
    )

    # Build a proper calendar date for time-series style analysis.
    df["date"] = pd.to_datetime(
        dict(year=df["year"], month=df["month"], day=df["day"]),
        errors="coerce"
    )

    df = df.drop(columns=["_raw_line_index"])
    return df


# ---------------------------------------------------------------------------
# STAGE 5: Validation
# ---------------------------------------------------------------------------

def validate(df):
    print("\n--- VALIDATION ---")
    print(f"Final shape: {df.shape[0]} records x {df.shape[1]} attributes")
    print(f"Records per region:\n{df['Region'].value_counts()}")

    print(f"\nDtypes:\n{df.dtypes}")

    missing_total = int(df.isna().sum().sum())
    print(f"\nMissing values per column:\n{df.isna().sum()}")

    dup_all = int(df.drop(columns=["record_repaired"]).duplicated().sum())
    dup_no_meta = int(df.drop(columns=["Region", "date", "record_repaired"]).duplicated().sum())
    print(f"\nFully duplicated rows (incl. Region/date): {dup_all}")
    print(f"Duplicated rows ignoring Region/date: {dup_no_meta}")

    print(f"\nUnique Classes values: {df['Classes'].unique()}")
    print(f"Classes distribution:\n{df['Classes'].value_counts()}")

    print(f"\nNumeric summary:\n{df.describe()}")

    out_of_range = df[(df["date"] < "2012-06-01") | (df["date"] > "2012-09-30")]
    print(f"\nRows with dates outside documented Jun-Sep 2012 range: {len(out_of_range)}")

    print(f"\nRecords flagged as reconstructed (record_repaired=True): "
          f"{int(df['record_repaired'].sum())}")

    # --- Hard invariants for this specific, documented dataset ---
    # These match the published dataset description (Abid, 2019; Abid &
    # Izeboudjen, 2020): 244 instances, 122 per region, binary class.
    assert df.shape[0] == 244, f"Expected 244 records, got {df.shape[0]}"
    assert missing_total == 0, f"Expected 0 missing values, found {missing_total}"
    assert dup_all == 0, f"Expected 0 duplicate rows, found {dup_all}"
    assert set(df["Region"].unique()) == {"Bejaia", "Sidi-Bel Abbes"}, \
        f"Unexpected region labels: {df['Region'].unique()}"
    assert (df["Region"].value_counts() == 122).all(), \
        f"Expected 122 records per region, got:\n{df['Region'].value_counts()}"
    assert set(df["Classes"].unique()) == {"fire", "not fire"}, \
        f"Unexpected class labels: {df['Classes'].unique()}"
    assert len(out_of_range) == 0, "Found dates outside the documented survey window"
    print("\nAll validation assertions passed.")

    return {
        "n_records": df.shape[0],
        "n_attributes": df.shape[1],
        "missing_total": missing_total,
        "duplicates": dup_all,
    }


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Clean the Algerian Forest Fires dataset.")
    parser.add_argument("--raw-path", default=DEFAULT_RAW_PATH,
                         help="Path to the raw UCI CSV file.")
    parser.add_argument("--output-path", default=DEFAULT_OUTPUT_PATH,
                         help="Path to write the cleaned CSV file.")
    args = parser.parse_args()

    raw_lines, columns = inspect_raw_file(args.raw_path)
    df_raw, malformed_rows, repaired = parse_regions(raw_lines, columns)

    print(f"\nParsed {len(df_raw)} data rows from raw file.")
    if malformed_rows:
        print(f"WARNING - unrepaired malformed rows: {malformed_rows}")
    else:
        print("All rows successfully parsed to the expected field count "
              "(after reconstruction where needed).")

    df_clean = clean_types(df_raw, columns)
    summary = validate(df_clean)

    df_clean.to_csv(args.output_path, index=False)
    print(f"\nCleaned dataset written to {args.output_path}")


if __name__ == "__main__":
    main()
