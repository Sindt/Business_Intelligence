# Business_Intelligence
## Assignment 1: Environment Setup and Introduction to Python


### 1. List the all files that this program generates:
IN:
```python
import assignment_1
import os

assignment_1.run()

os.listdir()
```

Output:

    ['.ipynb_checkpoints',
     'Assignment 1.ipynb',
     'assignment_1.py',
     'prices.png',
     'price_list.csv',
     'price_list.txt',
     'README.md',
     '__pycache__']

New files: **'prices.png',
     'price_list.csv',
     'price_list.txt',**


### 2. Describe which types of files this program generates and attach the contents of each file together with its name to your solution:

Type: .PNG
NAME: prices.png

IN:
```python
with open('prices.png', 'rb') as f:
    pngdata = f.read()
    print(len(pngdata))
```

Output:
    21862

