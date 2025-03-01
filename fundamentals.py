from scraper import get_json
from fetch_data import get_stock_namelist
from config import pd,bs

def script_fundamentals():
    script_name = get_stock_namelist()[1]
    url = f'https://sharehubnepal.com/data/api/v1/fundamental/values/{script_name}'
    fundamentals_json = (get_json(url)).get('data')
    print(script_name)
    print('------------------')
    for entry in fundamentals_json:
        fiscal_year = entry.get('fiscalYear')
        quarter = entry.get('quarter')
        each_quarter_data = entry.get('values')
        print(fiscal_year)
        print(quarter)
        print('------------------')

        for data in each_quarter_data:
            indicator = data.get('key')
            value = data.get('value')
        
            print(indicator , value)
        print('----------------------------------')

        
script_fundamentals()
