import pandas as pd

# Load CSV
nav = pd.read_csv("Data/Raw/02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Forward fill missing NAV
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

print("Rows after cleaning:", len(nav))

print("\nMissing NAV:")
print(nav["nav"].isnull().sum())

# Save cleaned file
nav.to_csv(
    "Data/Processed/02_nav_history_clean.csv",
    index=False
)

print("\nNAV cleaning completed!")

# ==========================
# Investor Transactions Cleaning
# ==========================

txn = pd.read_csv(
    "Data/Raw/08_investor_transactions.csv"
)

print("\nTransaction Columns:")
print(txn.columns)

print("\nTransaction Rows:")
print(len(txn))




# ==========================
# Investor Transactions Cleaning
# ==========================

txn = pd.read_csv(
    "Data/Raw/08_investor_transactions.csv"
)

# Fix date format
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Amount should be > 0
txn = txn[
    txn["amount_inr"] > 0
]

# Valid KYC values
print("\nKYC Values:")
print(txn["kyc_status"].unique())

print("\nTransaction Types:")
print(txn["transaction_type"].unique())

print("\nRows after cleaning:")
print(len(txn))

# Save cleaned file
txn.to_csv(
    "Data/Processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nTransaction Cleaning Completed!")
# ==========================
# Scheme Performance Check
# ==========================

perf = pd.read_csv(
    "Data/Raw/07_scheme_performance.csv"
)

print("\nPerformance Columns:")
print(perf.columns)

print("\nPerformance Rows:")
print(len(perf))

print("\nFirst 5 Rows:")
print(perf.head())
print("\nAll Columns:")
for col in perf.columns:
    print(col)

    # ==========================
# Scheme Performance Cleaning
# ==========================

perf = pd.read_csv(
    "Data/Raw/07_scheme_performance.csv"
)

# Convert returns to numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense Ratio Validation

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

# Flag anomalies

anomalies = perf[
    (perf["return_1yr_pct"] > 100)
    |
    (perf["return_1yr_pct"] < -100)
]

print("\nAnomalies Found:")
print(len(anomalies))

print("\nRows After Cleaning:")
print(len(perf))

# Save Clean File

perf.to_csv(
    "Data/Processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nPerformance Cleaning Completed!")