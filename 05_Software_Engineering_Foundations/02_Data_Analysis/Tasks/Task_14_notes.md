# Study Notes: Task_14

Generated Automatically


## Topic 1

### `Q-1:` Find the nearest element in the array to a given integer.
```
Ex:-
a=23 and array - [10 17 24 31 38 45 52 59].
Nearest element is 24
```
Hint: Read about this function `argmin()`

## Code Cell 2

```python
# code here
import numpy as np
arr = np.array([10 ,17, 24 ,31, 38, 45, 52, 59])
a = 23
print("Nearest Element = ")
nearest_element = abs(arr-a).argmin()
print(arr[nearest_element])
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 3

### `Q-2:` Replace multiples of 3 or 5 as 0 in the given array.
```
arr=[1 2 3 4 5 6 7 9]

result-> [1 2 0 4 0 0 7 0]
```

## Code Cell 4

```python
# code here
arr=np.array([1 ,2 ,3 ,4 ,5 ,6 ,7 ,9])

arr[(arr%3==0) | (arr%5==0)] = 0
arr
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 5

### `Q-3:` Use Fancy Indexing.
1. Double the array elements at  given indexes
```
arr = np.arrange(10)
indexes = [0,3,4,9]
```
Result -> `[ 0  1  2  6  8  5  6  7  8 18]`

2. Using a given array make a different array as in below example
```
array = [1,2,3]
result array -> [1 1 1 2 2 2 3 3 3]
```
* Internal-repetion should be as length of the array.

Hint:
```
if a is an array
a = [2,4]
a[[1,1,0,1]] will result in-> [4 4 2 4]
```

## Code Cell 6

```python
# code here
arr = np.arange(10)
indexes = [0,3,4,9]
arr[indexes] = arr[indexes] * 2
arr
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
arr = np.array([1,2,3])
arr1 = []
for i in range(len(arr)):
    arr1.extend([i]*len(arr))
arr[arr1]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 8

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 9

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 10

### `Q-4:` Your are given an array which is havig some nan value. You job is to fill those nan values with most common element in the array.
```
arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])

```

## Code Cell 11

```python
# code here
arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
arr

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
d={}
for i in arr.flatten():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
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
arr[np.isnan(arr)] = sorted(d.items(), key = lambda x: x[1])[-1][0]
arr
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 14

### `Q-5:` Write a NumPy program

- to find the missing data in a given array. Return a boolean matrix.
- also try to fill those missing values with 0. For that, you can use `np.nan_to_num(a)`

```python
import numpy as np

np.array([[3, 2, np.nan, 1],
          [10, 12, 10, 9],
          [5, np.nan, 1, np.nan]])
```

## Code Cell 15

```python
# code here
#1
arr = np.array([[3, 2, np.nan, 1],
          [10, 12, 10, 9],
          [5, np.nan, 1, np.nan]])
np.isnan(arr)
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
#2
np.nan_to_num(arr)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 17

### `Q-6:` Given two arrays, X and Y, construct the Cauchy matrix C.
`Cij =1/(xi - yj)`

http://en.wikipedia.org/wiki/Cauchy_matrix
```
x = numpy.array([1,2,3,4]).reshape((-1, 1)
y = numpy.array([5,6,7])
```

## Code Cell 18

```python
# code here
x = np.array([1,2,3,4]).reshape((-1, 1))
y = np.array([5,6,7])

1/(x-y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 19

### `Q-7:` Plot this below equation.

$$\large y = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

**Note: This equation is called tanh activation function. In deep learning, many times this function is used. If you find some difference between the sigmoid function and this tanh function, note that to your notebook.**

## Code Cell 20

```python
# code here
import matplotlib.pyplot as plt

x = np.linspace(-30, 30, 1000)
y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 21

### `Q-8:` Plot the below equation.

$$\large y = \sqrt{36 - (x - 4)^2} + 2$$

The range of x should be between -2 to 10. $x ∈ [-2, 10]$



## Code Cell 22

```python
# code here
x = np.linspace(-2, 10, 100)
y = np.sqrt(36 - (x-4)**2) + 2

plt.plot(x,y)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

### `Q-9:` Write a program implement Boradcasting Rule to check if two array can be added or not.
Given tuples of shapes.
```
shape of a- (3,2,2)
shape of b- (2,2)

check_broadcast(a, b) -> return Boolean (True if can broadcasted, False other wise.)
```

## Code Cell 24

```python
# code here

# 4 3 3 5
#     2 5

# Align both shapes
# Loop for both shapes from behind
#     If two numbers are not equal and none of the numbers are 1, return false
# return true

def check_broadcast(a,b):
    a = a[::-1]
    b = b[::-1]
    for ai, bi in zip(a,b):
        if ai != bi and ai != 1 and bi != 1:
            return False
    return
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 25

```python
print(check_broadcast((3, 2, 2), (2, 2)))
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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

