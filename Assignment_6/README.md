# Business_Intelligence - Assigment 6

## Part 1





```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import json
import sklearn
with open('assignments/assignment_6/users.json') as data_file:    
    data = json.load(data_file)
    df = pd.DataFrame(data,columns=['created','karma', 'id'],dtype=object)

#Replacing id with value = count of unique values
df['id'] = df['id'].map(df['id'].value_counts())

#Take the first 5000, else we get an error
X = df[['created', 'id']][:5000]
Y = df[['karma']][:5000]


X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.20)

X_train = X_train.values.reshape(-1,2)
X_test = X_test.values.reshape(-1,2)
y_train = y_train.values.reshape(-1,1)

```


```python
model = sklearn.linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```


```python
sklearn.metrics.mean_absolute_error(y_test, y_pred)
```




    3957.9158644781655




```python
print('MSE: %.2f' % sklearn.metrics.mean_squared_error(y_test, y_pred))
```

    MSE: 42827054.00


## Part 2
```python
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=10)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```


```python
sklearn.metrics.mean_absolute_error(y_test, y_pred)
```




    3063.4234000000001




```python
print('MSE: %.2f' % sklearn.metrics.mean_squared_error(y_test, y_pred))
```

    MSE: 42827054.00

