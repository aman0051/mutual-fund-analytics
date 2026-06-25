import sqlite3

# Database se connect
conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

# Tables check karni hain
tables = [
    "nav_history",
    "investor_transactions",
    "scheme_performance"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

conn.close()