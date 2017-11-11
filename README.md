# Business_Intelligence - Assignment 5

## Part 1

<p>Report the a and b values and write four lines about what a and b represents and what the difference is between a and b.</p>



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
import json
from pprint import pprint
from sklearn.model_selection import train_test_split

with open('assignments/assignment_5/users.json') as data_file:    
    data = json.load(data_file)
    
df = pd.DataFrame.from_dict(data, orient='columns')
X = df['created']
Y = df['karma']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


```
