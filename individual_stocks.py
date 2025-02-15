from fetch_data import get_stock_namelist
from config import rq, bs, pd

def main():
    
    stock_name = get_stock_namelist()[2]
    individual_stocks_url = "https://sharehubnepal.com/company/"

    response = rq.get(individual_stocks_url + stock_name)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        
        general_data = General_Signals(soup)
        share_proportion = listed_share_proportion(soup)

        # Merging both dictionaries
        combined_data = {**general_data, **share_proportion}  

        # Creating a DataFrame
        stock_overview_df = pd.DataFrame(combined_data.items(), columns=['Metric', 'Value'])

        return stock_overview_df
    else:
        print(f"Unable to fetch data with response code = {response.status_code}")


def General_Signals(soup):
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

def listed_share_proportion(soup):
    # Finding the div with class "space-y-1 that was child of another div"
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


print(main())