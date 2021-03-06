
# coding: utf-8

# In[1]:

import bs4
import requests
import csv
import os

class Scraper:
    
    def __init__(self, url):
        self.url = url
        
    def parseToInt(self, text):
        try:
            return int(text)
        except ValueError:
            return text    

    def scrape(self):
        data = []
        
        
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
    
            price = self.parseToInt(cols[1].text.replace(".", ""))    
                
            cols_sell = str(cols[2]).replace("<br/>", ">").split('>')
    
            sell_date = cols_sell[2]
    
            sell_type = cols_sell[3].replace("</h5", "")
    
            price_per_sq_m = self.parseToInt(cols[3].text.replace(".",""))
    
            no_rooms = self.parseToInt(cols[4].text)
        
            housing_type = cols[5].text
    
            size_in_sq_m = self.parseToInt(cols[6].text)
    
            year_of_contruction = self.parseToInt(cols[7].text)   
    
            price_change_in_pct = cols[8].text.replace("\n", "").strip()
    
            decoded_row = (street_str, zip_code, price, sell_date,sell_type, price_per_sq_m, no_rooms,
                           housing_type, size_in_sq_m, year_of_contruction, price_change_in_pct)
            data.append(decoded_row)
        
        return data;
    
class Main:
    
    def getHtmls(host):
        
        htmlList = []
        
        r = requests.get(host)
        soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')

        table_body = soup.find('body')
        rows = table_body.find('table').find('tbody').find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 1:
                if ".html" in cols[1].text:
                    htmlList.append(cols[1].text)
                
        
        return htmlList
      
    host = 'http://138.197.184.35/boliga/'
    htmls = getHtmls(host)

    def save_to_csv(data, path):
    
        if os.path.exists(path):
            with open(path, 'a', encoding='utf-8') as output_file:
                output_writer = csv.writer(output_file)
                for row in data:
                    output_writer.writerow(row)
        else:
            with open(path, 'w', encoding='utf-8') as output_file:
                output_writer = csv.writer(output_file)
                output_writer.writerow(['street_str', 'zip_code', 'price', 'sell_date','sell_type', 'price_per_sq_m', 'no_rooms',
                                   'housing_type', 'size_in_sq_m', 'year_of_contruction', 'price_change_in_pct'])

                for row in data:
                    output_writer.writerow(row)
    
    
    out_dir = './out'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    for html in htmls:
        url = os.path.join(host, html)
        scraper = Scraper(url)
        data = scraper.scrape()   
        save_to_file = os.path.join(out_dir, os.path.basename(html).split('_')[0] + '.csv')
        save_to_csv(data, save_to_file) 
    
