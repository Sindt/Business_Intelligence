# Business_Intelligence - Assignment 5

## Part 1


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
    df = pd.DataFrame(data,columns=['created','karma'],dtype=object)
    

df = df.fillna(lambda x: x.median())
X = df['created'][:10]
Y = df['karma'][:10]   


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

###Reshaping to 2d array
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)
y_test = y_test.values.reshape(-1, 1)

model = LinearRegression(normalize = True)
model.fit(X_train, y_train)

plt.scatter(X_train,y_train)
plt.plot(X_train, model.predict(X_train), color='red')
a = model.coef_[0]
b = model.intercept_[0]

print(a)
print(b)


Output:
[ -5.45604925e-05]
    79962.4223844

```
**Hældningskoefficienten a er grafens hældning. I vores eksempel er a negativ (-5.46) og derfor er vores funktion aftagende. b kan beskrives, som  den værdi hvor den lineære funktion skærer y-aksen. I vores eksempel 79962**


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

## Part 3


```python
from sklearn.metrics import mean_squared_error
from sklearn import linear_model

model = linear_model.LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

```python
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))
# Using a sample of 1000
Output: MSE: 74022065.02
```
