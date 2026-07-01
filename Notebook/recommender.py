import pandas as pd

performance = pd.read_csv("Data/Processed/07_scheme_performance_clean.csv")

print("Available Risk Grades:")
print(performance["risk_grade"].unique())

risk = input("\nEnter Risk (Low / Moderate / High): ")

result = performance[
    performance["risk_grade"].astype(str).str.lower() == risk.lower()
]

result = result.sort_values("sharpe_ratio", ascending=False)

print("\nTop 3 Recommended Funds:\n")
print(result[["scheme_name", "fund_house", "risk_grade", "sharpe_ratio"]].head(3))