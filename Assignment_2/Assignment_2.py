
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
    
    address = cols[0].find('a')
        
    address_str = str(address).replace("<br/>", ">").split('>')
        # WORKS
    street_str = address_str[1]
    zip_code = address_str[2].replace("</a", " ")
    
    try:
        price = int(cols[1].text)
    except ValueError:
        try:
            price = cols[1].text
        except ValueError:
            price = 'ERROR'

    decoded_row = (street_str, zip_code, price)
    data.append(decoded_row)
    
print(data[10])

