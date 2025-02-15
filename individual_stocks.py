from fetch_data import get_stock_data
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

def main():
    # Loading data in df
    stocks_df = get_stock_data()

    # Individual Stocks
    stock_list = stocks_df['symbol'].to_list()

    individual_stocks_url = "https://sharehubnepal.com/company/"

    response = rq.get(individual_stocks_url + stock_list[0])
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        
        fundamental_data = Fundamental_Signals(soup)


        # Extracting fundamental signals from the soup
        fundamental_df = pd.DataFrame(list(fundamental_data.items()), columns=['Analytical Name', 'Value'])
        return fundamental_df        
    else:
        print(f"Unable to fetch data with response code = {response.status_code}")


def Fundamental_Signals(soup):
    Fundamental_data = {}

    rows = soup.find_all('tr')

    for row in rows:
        # Finding td elements in each row
        td_elements = row.find_all('td')
        
        if len(td_elements) >= 2: 
            analytical_name = td_elements[0].text.strip()  # First column (key)   [LTP]
            analytical_value = td_elements[1].text.strip()  # Second column (value) [500.05]

            # Adding extracted value to dictionary
            Fundamental_data[analytical_name] = analytical_value

    return Fundamental_data
