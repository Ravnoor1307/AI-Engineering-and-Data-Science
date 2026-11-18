# Study Notes: 02_Numpy_Advanced

Generated Automatically


## Topic 1

### Numpy array vs Python lists

## Code Cell 2

```python
# speed
# list
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time

start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 3

```python
# numpy
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c = a + b
print(time.time()-start)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 4

```python
2.6730451583862305/0.17971158027648926
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 5

```python
# memory
a = [i for i in range(10000000)]
import sys

sys.getsizeof(a)
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
a = np.arange(10000000,dtype=np.int8)
sys.getsizeof(a)
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
# convenience
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

### Advanced Indexing

## Code Cell 9

```python
# Normal Indexing and slicing

a = np.arange(24).reshape(6,4)
a
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
a[1,2]
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
a[1:3,1:3]
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
# Fancy Indexing

a[:,[0,2,3]]
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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 14

```python
# Boolean Indexing
a = np.random.randint(1,100,24).reshape(6,4)
a
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 15

```python
# find all numbers greater than 50
a[a > 50]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 16

```python
# find out even numbers
a[a % 2 == 0]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 17

```python
# find all numbers greater than 50 and are even

a[(a > 50) & (a % 2 == 0)]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 18

```python
# find all numbers not divisible by 7
a[~(a % 7 == 0)]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 19

### Broadcasting

The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

The smaller array is “broadcast” across the larger array so that they have compatible shapes.

## Code Cell 20

```python
# same shape
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 21

```python
# diff shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 22

#### Broadcasting Rules

**1. Make the two arrays have the same number of dimensions.**<br>
- If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.<br>

## Topic 23

**2. Make each dimension of the two arrays the same size.**<br>
- If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
- If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.

## Topic 24

<img src = "https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png">

## Code Cell 25

```python
# More examples

a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 26

```python
a = np.arange(12).reshape(3,4)
b = np.arange(3)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 27

```python
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 28

```python
a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print(b)

print(a + b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 29

```python
a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 30

```python
a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 31

```python
a = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2,2)

print(a)
print(b)

print(a+b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 32

### Working with mathematical formulas

## Code Cell 33

```python
a = np.arange(10)
np.sin(a)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 34

```python
# sigmoid
def sigmoid(array):
  return 1/(1 + np.exp(-(array)))


a = np.arange(100)

sigmoid(a)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 35

```python
# mean squared error

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 36

```python
def mse(actual,predicted):
  return np.mean((actual - predicted)**2)

mse(actual,predicted)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 37

```python
# binary cross entropy
np.mean((actual - predicted)**2)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 38

```python
actual
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 39

### Working with missing values

## Code Cell 40

```python
# Working with missing values -> np.nan
a = np.array([1,2,3,4,np.nan,6])
a
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 41

```python
a[~np.isnan(a)]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 42

### Plotting Graphs

## Code Cell 43

```python
# plotting a 2D plot
# x = y
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = x

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 44

```python
# y = x^2
x = np.linspace(-10,10,100)
y = x**2

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 45

```python
# y = sin(x)
x = np.linspace(-10,10,100)
y = np.sin(x)

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 46

```python
# y = xlog(x)
x = np.linspace(-10,10,100)
y = x * np.log(x)

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 47

```python
# sigmoid
x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 48

### Meshgrids

## Code Cell 49

```python
# Meshgrids
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 50

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 51

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

