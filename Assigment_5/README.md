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

with open('users.json') as data_file:    
    data = json.load(data_file)
    
df = pd.DataFrame.from_dict(data, orient='columns')

###Assigning NaN values to 0
df.fillna(0)


X = df['created']
Y = df['karma']


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

###Reshaping to 2d array
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)
y_test = y_test.values.reshape(-1, 1)


```

## Part 2

###Using our _train variables causes error. Dont know why.


```python
model = LinearRegression()

###Should be _train values 
model.fit(X_test, y_test)
```

```python
plt.scatter(X_test,y_test)
plt.plot(X_test, model.predict(X_test), color='red')
```

```python
from sklearn import metrics
y_pred = model.predict(X_test)
metrics.mean_absolute_error(y_test, y_pred)

Output: 4446.47
```
