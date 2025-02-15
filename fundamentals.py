from fetch_data import get_stock_namelist
from config import pd
from scraper import get_json

stock_name = get_stock_namelist()[0]

url = "https://sharehubnepal.com/data/api/v1/fundamental/values/"+stock_name

data_dict = get_json(url)

data_values = data_dict['data']
df = pd.DataFrame(data_values[0]['values'])
print(df)