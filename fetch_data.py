from config import rq, pd, json
from scraper import get_json

def get_stock_namelist():
    stocks_df = get_stock_data()

    # Individual Stocks
    stock_list = stocks_df['symbol'].to_list()
    return stock_list


def get_stock_data():
    url = "https://sharehubnepal.com/live/api/v2/nepselive/live-nepse"
    data = get_json(url)
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