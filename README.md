# Business_Intelligence - Assigment 6

## Part 1

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

with open('assignments/assignment_6/users.json') as data_file:    
    data = json.load(data_file)
    df = pd.DataFrame(data,columns=['created','karma', 'id'],dtype=object)

#Replacing id with value = count of unique values
df['id'] = df['id'].map(df['id'].value_counts())

X = df[['created', 'id']]
Y = df[['karma']]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
```

