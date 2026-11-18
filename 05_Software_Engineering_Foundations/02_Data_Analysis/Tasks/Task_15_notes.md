# Study Notes: Task_15

Generated Automatically


## Topic 1

###`Q-1:` Create a random 3x4 matrix with value between 0-100. And perform below tasks

    i. Sort this matrix. np.sort()
    ii. Sort this matrix based on values in 2nd column.
    iii. Sort this matrix based on max value in each row.
    iv. Sort based on elements value.


## Topic 2

See examples:
```
arr =
    [[92 90 74]
    [ 6 63 93]
    [15 93 96]
    [70 60 48]]
```
```
i. np.sort
[[74 90 92]
 [ 6 63 93]
 [15 93 96]
 [48 60 70]]

ii. based on 2nd column
[[70 60 48]
 [ 6 63 93]
 [92 90 74]
 [15 93 96]]

iii. based on row max- ascending
[[15 93 96]
 [ 6 63 93]
 [92 90 74]
 [70 60 48]]

iv. based on elements value
[[ 6 15 48]
 [60 63 70]
 [74 90 92]
 [93 93 96]]

```

## Code Cell 3

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

###`Q-2:` There is an array of marks of 5 students in 4 subjects. Further you are asked to perform below task.
    i. Add marks every student of an extra subject in the same array.
    ii. Add two new students marks in respective 5 subjects.(one subject added in above task)
    iii. Add extra column with sum of all subjects(5-subjects) marks
    iv. Sort the array(non-ascending order) on total marks column--one added in above task. Show top 2 rows.

Note: Change dimension of arrays during concatenation or appending if required.

## Topic 5

Given Array-
```
marks = [[13, 10,  9, 33],
       [63, 46, 90, 42],
       [39, 76, 13, 29],
       [82,  9, 29, 78],
       [67, 61, 59, 36]]

extra_subject = [41, 87, 72, 36, 92]
#Two extra students record-
rec1 = [77, 83, 98, 95, 89]
rec2 = [92, 71, 52, 61, 53]
```

## Code Cell 6

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

###`Q-3:` Find unique arrays from a 2D array column wise and row wise.
```
arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])
```
Expected Result-
```
Row Wise
[[0 9 1 2 8 8]
 [1 2 3 3 1 1]
 [1 2 3 8 8 8]]

Col Wise
[[1 1 2 3 3]
 [0 8 9 1 2]
 [1 8 2 3 8]
 [1 1 2 3 3]]
```

## Code Cell 8

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 9

###`Q-4:` Flip given 2-D array along both axes at the same time.

## Code Cell 10

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

### `Q-5:` Get row numbers of NumPy array having element larger than X.
```
arr = [[1,2,3,4,5],
      [10,-3,30,4,5],
      [3,2,5,-4,5],
      [9,7,3,6,5]]

X = 6
```

## Code Cell 12

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 13

### `Q-6:` How to convert an array of arrays into a flat 1d array?


## Code Cell 14

```python
# These arrays are given.
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
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
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

### `Q-7:` You are given a array. You have to find the minimum and maximum array element and remove that from the array.

```python
import numpy as np

np.random.seed(400)
arr = np.random.randint(100, 1000, 200).reshape((1, 200))
```

## Code Cell 17

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 18

### `Q-8:` You are given an arrays. You have to limit this array's elements between 100 to 200. $arr ∈ [100, 700]$. So replace those values accordingly with the minimum and maximum value. Then sort the array and perform the cumulative sum of that array.

## Code Cell 19

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

### `Q-9:` You are given a array ($arr ∈ [0, 1]$). First you have round off the elements upto 3 decimal places and compare that
- 0th percentile == minimum value of the array
- 100th percentile == maximum value of the array
- also find the difference betwen 51th percenile and 50th percentile values

## Code Cell 21

```python
# code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

