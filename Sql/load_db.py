import pandas as pd
from sqlalchemy import create_engine

# Create Database
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Load Cleaned Files

nav = pd.read_csv(
    "Data/Processed/02_nav_history_clean.csv"
)

txn = pd.read_csv(
    "Data/Processed/08_investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "Data/Processed/07_scheme_performance_clean.csv"
)

# Save to SQLite

nav.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully!")