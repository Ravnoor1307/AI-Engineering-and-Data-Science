# Study Notes: week4_interview_questions

Generated Automatically


## Code Cell 1

```python
# 1. What do you mean by __name__ == '__main__'
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 2

### What is a module?

Any file with an extention of .py is called a module in python.

Whenever we execute a program it's module name is `__main__` and this name is stored in `__name__` variable

## Code Cell 3

```python
def display():
  print('hello')

display()
print(__name__)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

### Importing a module

- But what is the need to import a module?
- How to import a module

## Code Cell 5

```python
# import a module
import test
test.hello('nitish')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 6

```python
# import multiple module -> user defined + builtin
import math
import test

test.hello('nitish')
print(math.floor(4.3))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 7

```python
# show builtin modules
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

### Variations of import statement

## Code Cell 9

```python
# Normal
import math
import random
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 10

```python
# clubbing together
import math,random,test
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 11

```python
# importing specific names from module
from math import factorial,floor
from test import hello

print(factorial(5))
ceil(4.8)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 12

```python
# renaming modules
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


m.factorial(5)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 13

```python
from math import factorial as f

f(5)

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 14

### Order of execution of a module

## Code Cell 15

```python
import sys
for p in sys.path:
  print(p)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

### if `__name__` == `__main__`

## Code Cell 17

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 18

### What are packages in Python

A package in python is a directory containing similar sub packages and modules.

- A particular directory is treated as package if it has `__init__.py` file in it.
- The `__init__.py` file may be empty or contain some initialization code related to the package

## Code Cell 19

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

### What are 3rd party packages?

- The python community creates packages and make it available for other programmers
- PyPI -> Python Package Index
- You can upload your own package
- You can also install packages from PyPI and install using pip
- pip is a package manager utility
- it is automatically installed with python



## Code Cell 21

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

