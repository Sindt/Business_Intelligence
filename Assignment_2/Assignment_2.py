
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
    address_str = cols[0].text.strip()
    street_str = ' '.join(address_str.split(' ')[:-3])
    city_str = ' '.join(address_str.split(' ')[-3:])
    try:
        zip_number = int(address_str.split(' ')[-3])
    except ValueError:
         zip_number = 'ERROR'
        # Decode number of rooms
    no_rooms_str = cols[1].text.strip()
    
    try:
        no_rooms = int(no_rooms_str)
    except ValueError:
        no_rooms = 'ERROR'
        # Decode selling date and type
    size_in_sq_m_str = 'ERROR'
    try:
        size_in_sq_m = int(size_in_sq_m_str)
    except ValueError:
        size_in_sq_m = 'ERROR'
        
        # Decode year of construction
    year_of_construction_str = cols[3].text.strip()
    try:
        year_of_construction = int(year_of_construction_str)
    except ValueError:
        year_of_construction = 'ERROR'
        # Decode price
    price_str = cols[4].text.strip()
    price = float(price_str)   

        # Decode sales date
    sale_date_str = cols[5].text.strip()

    decoded_row = (street_str, city_str, zip_number, no_rooms,
                       size_in_sq_m, year_of_construction, price, 
                       sale_date_str)
    data.append(decoded_row)
    
    print('Scraped {} sales...'.format(len(data)))
    
print(data[15])


