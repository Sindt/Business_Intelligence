# Business_Intelligence - Assignment 7

## Part 1:


```python
import numpy as np
import pandas as pd
import nltk
nltk.download('vader_lexicon')
df = pd.read_csv('assignments/assignment_7/hn_items.csv',dtype={'text': str})

```

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
model = SentimentIntensityAnalyzer()
```


```python
#Get score foreach text
scores = [model.polarity_scores(text) for text in df['text'].astype(str)]

#Created df with score and the text
scores = pd.DataFrame(scores,df['text'])

#sorting
negative = scores.sort_values(by=['neg'],ascending=False)
postive = scores.sort_values(by=['pos'],ascending=False)

```


```python
#TOP 5 most negative:
negative[:5]
```
<p>Top 5 negative:</p>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>compound</th>
      <th>neg</th>
      <th>neu</th>
      <th>pos</th>
    </tr>
    <tr>
      <th>text</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fools.</th>
      <td>-0.4939</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>desperation</th>
      <td>-0.4588</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Desperation?</th>
      <td>-0.4588</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>dupe.</th>
      <td>-0.3612</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Ignorable.</th>
      <td>-0.2500</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>




```python
#TOP 5 most positive:
postive[:5]
```
<p>Top 5 positive:</p>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>compound</th>
      <th>neg</th>
      <th>neu</th>
      <th>pos</th>
    </tr>
    <tr>
      <th>text</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>nice!</th>
      <td>0.4753</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>yes</th>
      <td>0.4019</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>True</th>
      <td>0.4215</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>hilarious!\n</th>
      <td>0.4574</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>haha, cute.\n</th>
      <td>0.7184</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

## Part 2
<p>Forudsætter at part 1 er kørt først</p>

```python
df = pd.DataFrame(scores)

X = np.array(df[['pos','neg']])
y = np.array(df['neg'])
```

```python
from sklearn import preprocessing

lab_enc = preprocessing.LabelEncoder()
y = lab_enc.fit_transform(y)
```


```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X,y)
```

```python
import sklearn.metrics as metrics
metrics.accuracy_score(y, model.predict(X))
```
**Accuracy Score:**

    0.78959999999999997

## Part 3

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import folium
```

```python
df = pd.read_csv('assignments/assignment_7/boliga.zip', compression='zip')
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Index</th>
      <th>_1</th>
      <th>address</th>
      <th>zip_code</th>
      <th>price</th>
      <th>sell_date</th>
      <th>sell_type</th>
      <th>price_per_sq_m</th>
      <th>no_rooms</th>
      <th>housing_type</th>
      <th>size_in_sq_m</th>
      <th>year_of_construction</th>
      <th>price_change_in_pct</th>
      <th>lon</th>
      <th>lat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>Ved Volden 5, 5. TV</td>
      <td>1425 København K</td>
      <td>4000000</td>
      <td>23-05-2017</td>
      <td>Alm. Salg</td>
      <td>43956.0</td>
      <td>3.0</td>
      <td>Lejlighed</td>
      <td>91.0</td>
      <td>1938.0</td>
      <td>0.0</td>
      <td>12.593629</td>
      <td>55.671769</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Rådhusstræde 4C, 1</td>
      <td>1466 København K</td>
      <td>4895000</td>
      <td>18-05-2017</td>
      <td>Alm. Salg</td>
      <td>46619.0</td>
      <td>3.0</td>
      <td>Lejlighed</td>
      <td>105.0</td>
      <td>1796.0</td>
      <td>0.0</td>
      <td>12.573689</td>
      <td>55.676839</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>Store Kongensgade 112A, 3</td>
      <td>1264 København K</td>
      <td>250000</td>
      <td>15-05-2017</td>
      <td>Andet</td>
      <td>1851.0</td>
      <td>2.0</td>
      <td>Lejlighed</td>
      <td>135.0</td>
      <td>1860.0</td>
      <td>0.0</td>
      <td>12.590441</td>
      <td>55.687079</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>Amaliegade 13G, 2</td>
      <td>1256 København K</td>
      <td>7375000</td>
      <td>15-05-2017</td>
      <td>Alm. Salg</td>
      <td>75255.0</td>
      <td>3.0</td>
      <td>Lejlighed</td>
      <td>98.0</td>
      <td>1948.0</td>
      <td>9.0</td>
      <td>12.591287</td>
      <td>55.683439</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>Borgergade 144, 3. TH</td>
      <td>1300 København K</td>
      <td>5825000</td>
      <td>10-05-2017</td>
      <td>Alm. Salg</td>
      <td>57673.0</td>
      <td>3.0</td>
      <td>Lejlighed</td>
      <td>101.0</td>
      <td>1854.0</td>
      <td>3.0</td>
      <td>12.588744</td>
      <td>55.687623</td>
    </tr>
  </tbody>
</table>

```python
location_df = df[['lon','lat','price']]
location_df = location_df.fillna(0)
```

```python
my_map = folium.Map(location=[55.676098, 12.568337], zoom_start=10)
from folium.plugins import HeatMap
HeatMap(location_df.values.tolist()).add_to(my_map)
my_map
```
