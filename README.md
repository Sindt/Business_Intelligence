# Assignment 3

### 1) Geocode the the entire dataset
#### Setup

**Download osm og unzip**

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
import pandas as pd
import numpy as np

postcodes = defaultdict(lambda: defaultdict(dict))

pathboliga = "./data/boliga_all.csv"
pathosm = "./data/denmark-latest.osm"

def add_geocode():
    df = pd.read_csv(pathboliga)

    tdataframe = df

    tdataframe['lat'] = np.nan
    tdataframe['lon'] = np.nan

    dataframe = concat(tdataframe)

    dataframe.set_index("api_addresses", inplace=True)

    for idx, decoded_node in enumerate(decode_node_to_csv(pathosm)):
        try:
            geocoded_address = (decoded_node.tags['addr:street'] + " " + decoded_node.tags['addr:housenumber'] + " " + \
                           decoded_node.tags['addr:postcode'] + " " + decoded_node.tags['addr:city'], decoded_node.lon, decoded_node.lat)

            #print(geocoded_address[0])
            if dataframe.loc[geocoded_address[0]] is not None:
                dataframe.set_value(geocoded_address[0], 'lon', geocoded_address[1])
                dataframe.set_value(geocoded_address[0], 'lat', geocoded_address[2])

            #print(dataframe)
        except (KeyError, ValueError):
            pass

    dataframe.to_csv("./data/geo_data.csv", sep=',', encoding='utf-8')


def decode_node_to_csv(file):
    for entry in parse_file(file):

        if (isinstance(entry, Node) and
                    'addr:street' in entry.tags and
                    'addr:postcode' in entry.tags and
                    'addr:housenumber' in entry.tags and
                    'addr:city' in entry.tags):
            yield entry

def concat(dataframe):
    api_addresses = [' '.join([a.split(',')[0], z]) for a, z in dataframe[['street_str', 'zip_code']].values]
    dataframe = dataframe.assign(api_addresses=api_addresses)
    dataframe = dataframe.drop_duplicates(subset="api_addresses")

    return dataframe


add_geocode()

```

**Result:**
<br>
Bla bla bla


### 2) Convert all sales dates in the dataset into proper datetime
```python
df["sell_date"] = pd.to_datetime(df["sell_date"], dayfirst=True, errors='coerce')
```

### 3) Compute the average price per square meter for the years 1992 and 2016
**Result:**
<br>
Bla bla bla

### 4) Create, four new CSV files containing the sales data of, Copenhagen, Odense, Aarhus, and Aalborg.
```python
import pandas as pd
df = pd.read_csv('boliga_all.csv')

df.index = df['sell_date']
del df['sell_date']

def to_csv(data, name):
    try:
        data.to_csv(name + '.csv', sep='\t')
    except:
        print('Error')
    
to_csv( df[df['zip_code'] == '1050 København K']['1992'],'1050')   
to_csv( df[df['zip_code'] == '5000 Odense C']['1992'],'5000')   
to_csv( df[df['zip_code'] == '8000 Aarhus C']['1992'],'8000')   
to_csv( df[df['zip_code'] == '9000 Aalborg']['1992'],'9000')    
```

### 5) Create a 2-dimensional scatter plot
**Result:**
<br>
Bla bla bla

### 6) Use the following function, which computes the Haversine Distance
**Result:**
<br>
Bla bla bla

