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
