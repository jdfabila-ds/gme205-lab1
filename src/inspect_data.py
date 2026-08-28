import os
import json
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Paths
# ----------------------------
DATA_PATH = "data/points.csv"
OUTPUT_DIR = "output"
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "summary.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "preview.png")

# ----------------------------
# A. Read the CSV file
# ----------------------------
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: Cannot find file at '{DATA_PATH}'.")
    print("Make sure you have: data/points.csv")
    raise

print("=== DATA INSPECTION REPORT ===")

# ----------------------------
# B. Print basic information
# ----------------------------
num_rows, num_cols = df.shape

print("\nBasic Information")
print("-----------------")
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print(f"Column names: {list(df.columns)}")


# ----------------------------
# C. Data quality checks
# ----------------------------
print("\nData Quality Checks")
print("-------------------")

missing_values = df.isna().sum()
print("Missing values per column:")
print(missing_values)

# Ensure required columns exist
required_cols = {"lon", "lat"}
if not required_cols.issubset(df.columns):
    missing = required_cols - set(df.columns)
    raise ValueError(f"Missing required column(s): {missing}. Required: lon, lat")

# Invalid coordinate checks (also catches missing lon/lat as invalid)
invalid_lon_mask = df["lon"].isna() | (df["lon"] < -180) | (df["lon"] > 180)
invalid_lat_mask = df["lat"].isna() | (df["lat"] < -90) | (df["lat"] > 90)

invalid_lon_count = int(invalid_lon_mask.sum())
invalid_lat_count = int(invalid_lat_mask.sum())

print(f"\nInvalid longitude values (missing or outside -180..180): {invalid_lon_count}")
print(f"Invalid latitude values (missing or outside -90..90): {invalid_lat_count}")
