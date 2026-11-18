# Study Notes: Task_01_Solutions

Generated Automatically


## Topic 1

# Task : Session 1
Solve these questions own your own and try to test yourself what you have learned in the session.

Happy Learning!

## Topic 2

### Q1 :- Print the given strings as per stated format.

**Given strings**:
```
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
```
**Output**:
```
Data-Science-Mentorship-Program-started-By-CampusX
```

Concept- [Seperator and End]

## Code Cell 3

```python
# Write your code here
print("Data","Science","Mentorship","Program",sep='-',end='-started-')
print("By","CampusX",sep='-')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

### Q2:- Write a program that will convert celsius value to fahrenheit.

## Code Cell 5

```python
# Write your code here
celcius = float(input('enter the temp in celcius'))

faren = celcius * (9/5) + 32

print(faren,'F')

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 6

### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

## Code Cell 7

```python
# Write your code here

a = 3
b = 5

temp = a
a = b
b = temp

print(a)
print(b)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

## Code Cell 9

```python
# Write your code here
p1x = int(input('enter x cood of 1st point'))
p1y = int(input('enter y cood of 1st point'))
p2x = int(input('enter x cood of 2nd point'))
p2y = int(input('enter y cood of 2nd point'))

distance = ((p2x - p1x)**2 + (p2y - p1y)**2)**0.5

print(round(distance,2))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 10

### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

Hint - si = (p * t * r)/100


## Code Cell 11

```python
# Write your code here
p = int(input('Enter amount'))
t = int(input('Enter time period'))
r = float(input('Enter rate'))

interest = (p*t*r)/100

print('the interest is',interest)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 12

### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2





## Code Cell 13

```python
# Write your code here
heads = 4
legs = 12

# chicken + dog = head
# 2*chicken + 4*dog = legs
# 2*head - 2*dog + 4*dog = legs
# dog = legs/2 - head
# chicken = 2*head - legs/2
dog = legs/2 - heads
chicken = 2*heads - legs/2
print('Dogs : ',int(dog))
print('Chickens : ',int(chicken))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 14

### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

Hint - Thus, the sum of the squares of first n natural numbers =  n(n+1)(2n+1)/6

## Code Cell 15

```python
# Write your code here
n = int(input('enter the number'))

result = (n*(n+1)*(2*n + 1))/6
print(result)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 16

### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

Hint - an = a + (n – 1)d

## Code Cell 17

```python
# Write your code here
first_term = int(input('enter 1st term'))
second_term = int(input('enter 2nd term'))
n = int(input('enter the value of n'))

d = second_term - first_term

an = first_term + (n-1)*d

print(an)


```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 18

### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

## Code Cell 19

```python
# Write your code here
n1 = int(input('num1'))
d1 = int(input('den1'))
n2 = int(input('num2'))
d2 = int(input('den2'))

rn = n1*d2 + n2*d1
rd = d1*d2

print('{}/{}'.format(rn,rd))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.



Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm

## Code Cell 21

```python
# Write your code here
import math

h_t = float(input('height'))
b_t = float(input('breadth'))
l_t = float(input('length'))

h_g = float(input('height of glass'))
r_g = float(input('radius of the glass'))

vol_tank = h_t*b_t*l_t
vol_glass = 3.14*r_g*r_g*h_g

print('no of glasses',math.floor(vol_tank/vol_glass))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 22

```python
math.floor(6.7)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 23

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

