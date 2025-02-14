import requests
import json
import pandas as pd

url = "https://sharehubnepal.com/live/api/v2/nepselive/live-nepse"
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    df = pd.DataFrame(json_data)
    print(df['data'])
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")

