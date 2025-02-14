from fetch_data import get_stock_data
import pandas as pd
import requests as rq

# loading data in df
stocks_df = get_stock_data()

# Individual Stocks

stock_list = stocks_df['symbol'].to_list()

individual_stocks_url = "https://sharehubnepal.com/company/"

response = rq.get(individual_stocks_url+stock_list[0])
print(response.status_code)