# Assignment 3

### 1) Geocode the the entire dataset
#### Setup

**Download som og unzip**

```python
%%bash
wget --directory-prefix=./data/ http://download.geofabrik.de/europe/denmark-latest.osm.bz2
bzip2 -d ./data/denmark-latest.osm.bz2
```

**Installation af osmread**

```python
%%bash
sudo pip install osmread
```

**Data fra csv fil (Kan findes i zip under Assigment_3 folder:**

```python
import pandas as pd
df = pd.read_csv('boliga_all.csv')
df.head()
```

**Data fra osm fil**

```python
from osmread import parse_file, Node
from collections import defaultdict

postcodes = defaultdict(lambda: defaultdict(dict))

def decode_node_to_csv():
    for entry in parse_file('./data/denmark-latest.osm'):
        if (isinstance(entry, Node) and 
            'addr:street' in entry.tags and 
            'addr:postcode' in entry.tags and 
            'addr:housenumber' in entry.tags):
                yield entry


for idx, decoded_node in enumerate(decode_node_to_csv()):
    postcodes[decoded_node.tags['addr:postcode']][decoded_node.tags['addr:street']][decoded_node.tags['addr:housenumber']] = decoded_node.lon, decoded_node.lat
            
```

**Result:**
<br>
Bla bla bla


### 2) Convert all sales dates in the dataset into proper datetime
```python
df["sell_date"] = pd.to_datetime(df["sell_date"], dayfirst=True, errors='coerce')
```

### 3) Compute the average price per square meter for the years 1992 and 2016
```python
import numpy as np

df['zip_nr'] = [int(el.split(' ')[0]) for el in df['zip_code'].values]

mask92 = (df["sell_date"].dt.year == 1992) & (df['price_per_sq_m'] != '-') & (~df['price_per_sq_m'].isnull())
mask16 = (df["sell_date"].dt.year == 2016) & (df['price_per_sq_m'] != '-') & (~df['price_per_sq_m'].isnull())

city_code92 = np.unique(df[mask92].zip_nr)
city_code16 = np.unique(df[mask16].zip_nr)

mean92 = df[mask92].groupby(["zip_nr"]).price_per_sq_m.mean()
mean16 = df[mask16].groupby(["zip_nr"]).price_per_sq_m.mean()

city_names = ["København", "Odense", "Aarhus", "Aalborg"]
zips = [1050, 5000, 8000, 9000]

df_avg92 = pd.DataFrame({'city_code': city_code92,
                        'city': city_names,
                        'zip': zips},
                        columns=['city_code', 'city', 'zip'],
                        index=city_code
                       )
df_avg92 = df_avg92.join(pd.DataFrame(mean92))
df_avg92.rename(columns={'price_per_sq_m': 'Average'}, inplace=True)


df_avg16 = pd.DataFrame({'city_code': city_code16,
                        'city': city_names,
                        'zip': zips},
                        columns=['city_code', 'city', 'zip'],
                        index=city_code
                       )
df_avg16 = df_avg16.join(pd.DataFrame(mean16))
df_avg16.rename(columns={'price_per_sq_m': 'Average'}, inplace=True)

df_avg92
df_avg16
```
**Result:**
<br>
The code is not complete for this exercise at the point of hand-in, but it should be almost solved with the code above.


### Create, four new CSV files containing the sales data of, Copenhagen, Odense, Aarhus, and Aalborg.
**Result:**
<br>
Bla bla bla

### Create a 2-dimensional scatter plot
**Result:**
<br>
Bla bla bla

### Use the following function, which computes the Haversine Distance
**Result:**
<br>
Bla bla bla

