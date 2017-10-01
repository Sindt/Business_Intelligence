# Assignment 4: Data Visualisation


Udpak zip fil med boliga loc data:

```python
%%bash

bzip2 -d ./data/boliga_all_loc.csv.bz2

```


### 1) Create a plot with the help of Basemap


### 2) Use folium to plot the locations of the 1992 housing sales for the city centers of Copenhagen

```python
%%bash

sudo pip install folium

```
```python
import pandas as pd
import folium


complete_data = './data/boliga_all_loc.csv'

df = pd.read_csv(complete_data)

dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')

df = pd.read_csv(complete_data, parse_dates=['sell_date'], date_parser=dateparse)

df.index = df['sell_date']
del df['sell_date']


df1 = [df[df['zip_code'] == '1050 København K']['1992'], df[df['zip_code'] == '5000 Odense C']['1992'],df[df['zip_code'] == '8000 Aarhus C']['1992'],   
df[df['zip_code'] == '9000 Aalborg']['1992']]
       
result = pd.concat(df1)

mask = ((~result.lat.isnull()) & (~result.lon.isnull())) 
result_1992 = result[mask]        

my_map = folium.Map(location=[55.88207495748612, 10.636574309440173], zoom_start=7)

for coords in zip(result_1992.lon.values, 
                  result_1992.lat.values):
    folium.CircleMarker(location=[coords[1], coords[0]], radius=2).add_to(my_map)
my_map.save('data/1992.html')
my_map    
```


### 3) Create a 2D plot


### 4) Create a histogram (bar plot)


### 5) Create a cumulatve histogram


### 6) Create a 3D histogram


### 7) Freestyle - Create a plot


