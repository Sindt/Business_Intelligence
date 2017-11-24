# Business_Intelligence - Assignment 7

## Part 1:


```python
import numpy as np
import pandas as pd
import nltk
nltk.download('vader_lexicon')
```

```python
df = pd.read_csv('assignments/assignment_7/hn_items.csv',dtype={'text': str})
from nltk.sentiment.vader import SentimentIntensityAnalyzer
model = SentimentIntensityAnalyzer()
```


```python
scores = [model.polarity_scores(text) for text in df['text'].astype(str)]
scores = pd.DataFrame(scores)
negative = scores.sort_values(by=['neg'],ascending=False)
postive = scores.sort_values(by=['pos'],ascending=False)
```


```python
negative.head()
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
  </thead>
  <tbody>
    <tr>
      <th>8932</th>
      <td>-0.4939</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4516</th>
      <td>-0.4588</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7326</th>
      <td>-0.4588</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4505</th>
      <td>-0.3612</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5750</th>
      <td>-0.2500</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
postive.head()
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
  </thead>
  <tbody>
    <tr>
      <th>3656</th>
      <td>0.4753</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7893</th>
      <td>0.4019</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3025</th>
      <td>0.4215</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6001</th>
      <td>0.4574</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7612</th>
      <td>0.7184</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>


