import requests
import json
import pandas as pd

def get_stock_data():
    url = "https://sharehubnepal.com/live/api/v2/nepselive/live-nepse"
    response = requests.get(url)
    
    # Handle successful response
    if response.status_code == 200:
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Error: Response is not a valid JSON.")
            return None
        
        # Extracting the list from "data" key
        stocks = data.get("data", [])
        
        if stocks:
            # Convert to Pandas DataFrame
            df = pd.DataFrame(stocks)
            # Optional: Filter for specific columns if required
            df = df[["symbol", "securityName", "sector"]]
            return df
        else:
            print("No stock data found.")
            return None
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None
