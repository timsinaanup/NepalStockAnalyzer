from fetch_data import get_stock_namelist
from config import *
from scraper import get_soup

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Runs browser in background without opening a window
options.add_argument('--disable-gpu')

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

stock_name = get_stock_namelist()[0]
url = f"https://sharehubnepal.com/company/{stock_name}/fundamental-analysis/reports"

driver.get(url)

# Optional: Wait for some content to load dynamically (e.g., waiting for a specific element)
time.sleep(5)  # Give some time for content to load (you can adjust the wait time as needed)

# Now you can interact with the page using BeautifulSoup or by using Selenium directly
page_source = driver.page_source  # Get the entire HTML content after JavaScript loads

soup = bs(page_source, 'html.parser')


table = soup.find('table', class_="min-w-max w-full caption-bottom border-collapse") 
thead = table.find('thead', class_= "dark:bg-dark-container bg-white dark:text-text-light border-b h-8 text-sm font-bold uppercase")
tbody = table.find('tbody', class_="dark:text-text-light text-black font-bold text-xs")
th_tr = thead.find('tr', class_ = 'hover:bg-muted/50 border-b dark:border-gray-700 border-gray-200')

headers = [th.text.strip() for th in th_tr.find_all('th')]  # Extract column headers

