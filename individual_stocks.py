from fetch_data import get_stock_data
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
# loading data in df
stocks_df = get_stock_data()

# Individual Stocks

stock_list = stocks_df['symbol'].to_list()

individual_stocks_url = "https://sharehubnepal.com/company/"

response = rq.get(individual_stocks_url+stock_list[0])
if response.status_code == 200:
    print("inside each script sucessfully")
else:
    print(f"Unable to fetch data wuth response.code = {response.code}")
