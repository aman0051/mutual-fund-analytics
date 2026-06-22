import requests
import pandas as pd

url = "https://api.mfapi.in/mf/119551"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("API Connected Successfully")
    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

else:
    print("API Error")