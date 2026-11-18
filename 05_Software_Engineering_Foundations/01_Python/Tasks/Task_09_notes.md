# Study Notes: Task_09

Generated Automatically


## Topic 1

### `Problem-1:` Class inheritence

Create a **Bus** child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

## Code Cell 2

```python
# Write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 3

### `Problem-2:` Class Inheritence

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of *Bus.seating_capacity()* a default value of 50.

Use the following code for your parent Vehicle class.

## Code Cell 4

```python

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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 6

### `Problem-3:` Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.

## Code Cell 7

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

### `Problem-4:` Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.

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

### `Problem-5:` Write a program with class Bill. The users have the option to pay the bill either by cheque or by cash. Use the inheritance to model this situation.

## Code Cell 11

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 12

###`Q-6:` FlexibleDict
As of now we are accessing values from dictionary with exact keys. Now we want to amend accessing values functionality. if a dict have key `1` (int) the even if we try to access values by giving `'1'` (1 as str) as key, we should get the same result and vice versa.

Write a class `FlexibleDict` upon builtin `dict` class with above required functionality.

Hint- `dict[key] => dict.__getitem__(key)`

## Topic 13

Ex.
```
fd = FlexibleDict()
fd['a'] = 100
print(fd['a']) # Like regular dict

fd[5] = 500
print(fd[5]) # Like regular dict

fd[1] = 100
print(fd['1']) # actual Key is int but still trying to access through str key.
fd['1'] = 100
print(fd[1])

```
`Output:`
```
100
500
100
100

```

## Code Cell 14

```python

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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

