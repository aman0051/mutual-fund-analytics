import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(csv_files)}\n")

for file in csv_files:
    print("=" * 60)
    print("File Name:", file)

    file_path = os.path.join(folder_path, file)

    try:
        df = pd.read_csv(file_path)

        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:", df.duplicated().sum())

    except Exception as e:
        print("Error:", e)

print("\nData Ingestion Completed Successfully!")
