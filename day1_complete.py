import pandas as pd
import requests

# Load Fund Master Dataset
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")

print("\n===== UNIQUE FUND HOUSES =====")
print(fund_master["fund_house"].unique())

print("\n===== UNIQUE CATEGORIES =====")
print(fund_master["category"].unique())

print("\n===== UNIQUE SUB CATEGORIES =====")
print(fund_master["sub_category"].unique())

print("\n===== UNIQUE RISK GRADES =====")
print(fund_master["risk_category"].unique())

print("\n===== AMFI CODE VALIDATION =====")

nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("SUCCESS: All AMFI codes from fund_master exist in nav_history")
else:
    print("Missing Codes:")
    print(missing_codes)

   

print("\n===== FETCHING NAV DATA =====")

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, amfi_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"Data/Raw/{scheme_name}_NAV.csv"

        nav_df.to_csv(filename, index=False)

        print(f"{scheme_name} NAV saved successfully")

    else:
        print(f"Failed to fetch {scheme_name}")