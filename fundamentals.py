from scraper import get_json
from fetch_data import get_stock_namelist
from config import pd,bs

def script_fundamentals():
    script_name = get_stock_namelist()[52]
    url = f'https://sharehubnepal.com/data/api/v1/fundamental/values/{script_name}'
    fundamentals_json = get_json(url)
    return fundamentals_json.get('data')[0]
    
    
print(script_fundamentals())