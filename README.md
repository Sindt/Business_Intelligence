# Assignment 4: Data Visualisation


Udpak zip fil med boliga loc data:

```python
%%bash

bzip2 -d ./data/boliga_all_loc.csv.bz2

```


### 1) Create a plot with the help of Basemap

```python
 import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = './data/boliga_all_loc.csv'

dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')

df = pd.read_csv(data, parse_dates=['sell_date'], date_parser=dateparse)

df['sell_year'] = df['sell_date'].dt.year

df.head()

## Approx. within 50 km
mask = ((df['sell_year'] == 2015) &
        (df['lat'] <= 56.128313) &
        (df['lat'] >= 55.223909) &
        (df['lon'] <= 13.020535) &
        (df['lon'] >= 12.116131))
df_copenhagen = df[mask]
df_copenhagen.head()


x_values = df_copenhagen['lon']
y_values = df_copenhagen['lat']

plt.scatter(x_values[:], y_values[:], s=1, edgecolor='none')


plt.plot()

plt.show()


```

![alt text](https://i.imgur.com/lNHglMR.png)


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


df1 = [df[df['zip_code'] == '1050 KÃ¸benhavn K']['1992'], df[df['zip_code'] == '5000 Odense C']['1992'],df[df['zip_code'] == '8000 Aarhus C']['1992'],   
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

hypothesis:
It would be expected that the price_per_sq_m will decrease when the distance to nørreport increases, because you get further and further from the city center towards the outskirts of the city. 



```python
import math
import matplotlib.pyplot as plt
%matplotlib notebook


def haversine_distance(origin, destination):

    lat_orig, lon_orig = origin
    lat_dest, lon_dest = destination
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig))
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def plot_values(x, y):

    plt.plot(x,y, 'ro')
    plt.axis([0, 80000, 0, 8000])
    plt.show()    
    


mask = ((df_zealand_00_05['sell_year'] == 2005) &
            (~df_zealand_00_05['price_per_sq_m'].isnull()) &
            (df_zealand_00_05['price_per_sq_m'] < 80000) &
            (df_zealand_00_05['zip_nr'] < 3000))

prices = df_zealand_00_05[mask]['price_per_sq_m']

df['dist_to_center'] = [haversine_distance((55.6837, 12.5716), el) 
             for el in df[mask][['lon', 'lat']].values]


df3 = df[mask][['price_per_sq_m','dist_to_center']]

df3.sort_values(by=['price_per_sq_m'])

plot_values(df3['price_per_sq_m'], df3['dist_to_center'])

```

Conclusion:
When calculating the distance to nørreport from the geolocations in the dataset, we ended up with distances which where quite similar across the whole dataset. This points to an error in the calculation, but it has not been possible to locate it.


### 4) Create a histogram (bar plot)


### 5) Create a cumulatve histogram


### 6) Create a 3D histogram


### 7) Freestyle - Create a plot


