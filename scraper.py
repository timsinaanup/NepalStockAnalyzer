from config import bs, rq , json

def get_soup(url):
    response = rq.get(url)
    if response.status_code == 200:
            return bs(response.text, 'html.parser') 

    else :
          return f'Error fetching data with response.status_code : {response.status_code}'

def get_json(url):
    response = rq.get(url)
    if response.status_code == 200: 
        try:
            data = response.json() 
            return data
        except json.JSONDecodeError:
            print("Error: Response is not a valid JSON.")
            return None
        
      