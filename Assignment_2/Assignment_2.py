
# coding: utf-8

# In[1]:

import bs4
import requests
from IPython.display import IFrame

class Scraper:
    
    def __init__(self, url):
        self.url = url
        
    def parseToInt(text):
        try:
            return int(text)
        except ValueError:
            return text    

    def scrape(self):
        data = []
        
        IFrame(self.url, width=700, height=400)
        
        r = requests.get(self.url)
        soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')

        table_body = soup.find('body')
        rows = table_body.find('table').find('tbody').find_all('tr')

        for row in rows:
            cols = row.find_all('td')
       
            address = cols[0].find('a')    
            address_str = str(address).replace("<br/>", ">").split('>')
            street_str = address_str[1]
    
            zip_code = address_str[2].replace("</a", "")
    
            price = parseToInt(cols[1].text.replace(".", ""))    
                
            cols_sell = str(cols[2]).replace("<br/>", ">").split('>')
    
            sell_date = cols_sell[2]
    
            sell_type = cols_sell[3].replace("</h5", "")
    
            price_per_sq_m = parseToInt(cols[3].text.replace(".",""))
    
            no_rooms = parseToInt(cols[4].text)
        
            housing_type = cols[5].text
    
            size_in_sq_m = parseToInt(cols[6].text)
    
            year_of_contruction = parseToInt(cols[7].text)   
    
            price_change_in_pct = cols[8].text.replace("\n", "").strip()
    
            decoded_row = (street_str, zip_code, price, sell_date,sell_type, price_per_sq_m, no_rooms,
                           housing_type, size_in_sq_m, year_of_contruction, price_change_in_pct)
            data.append(decoded_row)
    
        print(data[1])
        print(data[10])
        print(data[37])
   
    
class main:
    scraper = Scraper('http://138.197.184.35/boliga/2650_38.html')
    
    scraper.scrape()




