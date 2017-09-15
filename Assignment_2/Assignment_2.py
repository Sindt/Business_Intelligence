
# coding: utf-8

# In[1]:

import bs4
import requests
from IPython.display import IFrame

url = 'http://138.197.184.35/boliga/1050-1549_1.html'
IFrame(url, width=700, height=400)

url = 'http://138.197.184.35/boliga/1050-1549_1.html'
r = requests.get(url)
soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')

data = []

table_body = soup.find('body')
rows = table_body.find('table').find('tbody').find_all('tr')

for row in rows:
    cols = row.find_all('td')
        #address,zip_code,price,sell_date,sell_type,price_per_sq_m,no_rooms,housing_type,size_in_sq_m,year_of_construction,price_change_in_pct
    address = cols[0].find('a')
        
    address_str = str(address).replace("<br/>", ">").split('>')
        # WORKS
    street_str = address_str[1]
    zip_code = address_str[2].replace("</a", "")
    
    try:
        price = int(cols[1].text)
    except ValueError:
        try:
            price = cols[1].text
        except ValueError:
            price = 'ERROR'
                
    cols_sell = str(cols[2]).replace("<br/>", ">").split('>')
    
    sell_date = cols_sell[2]
    
    sell_type = cols_sell[3].replace("</h5", "")
    try:
        price_per_sq_m = int(cols[3].text)
    except ValueError:
        price_per_sq_m = cols[3].text
    
    try:
        no_rooms = int(cols[4].text)
    except ValueError:
        no_rooms = cols[4].text
        
        
    decoded_row = (street_str, zip_code, price, sell_date,sell_type, price_per_sq_m, no_rooms)
    data.append(decoded_row)
    
print(data[1])



