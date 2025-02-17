from fetch_data import get_stock_namelist
from config import rq, bs, pd
from scraper import get_json , get_soup

def main():
    
    stock_name = get_stock_namelist()[0]

    divident_details = divident_history(stock_name)
    general_data = General_Signals(stock_name)
    share_proportion = listed_share_proportion(stock_name)
    
    return None

def General_Signals(stock_name):
    url = "https://sharehubnepal.com/company/"+stock_name
    soup = get_soup(url)

    General_data = {}

    rows = soup.find_all('tr')

    for row in rows:
        # Finding td elements in each row
        td_elements = row.find_all('td')
        
        if len(td_elements) >= 2: 
            analytical_name = td_elements[0].text.strip()  # First column (key)   [LTP]
            analytical_value = td_elements[1].text.strip()  # Second column (value) [500.05]

            # Adding extracted value to dictionary
            General_data[analytical_name] = analytical_value

    
    return General_data

def listed_share_proportion(stock_name):
    # Finding the div with class "space-y-1 that was child of another div"
    url = "https://sharehubnepal.com/company/"+stock_name
    soup = get_soup(url)
    ownership_structure = {}
    proportion_table = (soup.find_all('div',class_="w-full dark:bg-dark-container bg-white md:p-5 p-2 rounded-md"))[2].find_all('div',class_="space-y-1")
    if len(proportion_table) == 4:
        for i in range(len(proportion_table)-1) :  
            Holder_name = proportion_table[i].find('h3', class_='font-medium text-base dark:text-gray-500 text-gray-600 inline-flex items-center gap-1').text
            Holder_percentage = proportion_table[i].find('p',class_='font-bold text-lg md:text-xl flex items-center gap-2').find('span').text[1:-1]
            
            ownership_structure[Holder_name] = Holder_percentage
    
    if len(proportion_table) == 3:
        for i in range(len(proportion_table)-1) :  
            Holder_name = proportion_table[i].find('h3', class_='font-medium text-base dark:text-gray-500 text-gray-600 inline-flex items-center gap-1').text
            Holder_percentage = proportion_table[i].find('p',class_='font-bold text-lg md:text-xl flex items-center gap-2').find('span').text[1:-1]
            ownership_structure[Holder_name] = Holder_percentage
        
    Total_listed_share = proportion_table[-1].find('p').text
    ownership_structure.update(
        {
            "Total Listed Share" : Total_listed_share
        }
    )

    return ownership_structure


def divident_history(stock_name):
    url = f"https://sharehubnepal.com/data/api/v1/dividend?symbol={stock_name}&limit=50"
    dividents_json = get_json(url)
    content_list = dividents_json.get('data', {}).get('content', [])  # Extract 'content' list
    dividents_df = pd.DataFrame(content_list)
    required_divident_details = ((dividents_df[['symbol','bonus', 'cash', 'total','listingDate','fiscalYear','status']])).to_json()
    return required_divident_details



main()