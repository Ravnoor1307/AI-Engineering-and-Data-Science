# Study Notes: Task_11_Solutions

Generated Automatically


## Topic 1

## Exception Handling


## Topic 2

### `Q-1`: You are given a function definition. There might be several issues on execution of this function. You are asked to do exception handling for diffrent errors that this function goes in to `without altering this function`. And print error text.



## Topic 3

Function parameters `l -> list, s -> could be anything`

```
def function(l: list, s, **args):
    last_element = l[-1]
    
    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10
    
    res = sum(l)
    
    p = args['p']
    # print(p)
    return res/last_element * p + any_element

```
Check for different function calls:-

```
function([1,2,1], 12)
function([1,2,1]*9, '1-2')
function([1,'2',1]*9, 12)
function([1,'2',1]*9, 12)
function([1,2,0]*9, 12  )
function([1,2,1]*9, 12, p=None)
function([1,2,0]*9, 12, p=10)
```

## Code Cell 4

```python
# Write code here
def function(l: list, s, **args):
    last_element = l[-1]

    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10

    res = sum(l)

    p = args['p']
    # print(p)
    return res/last_element * p + any_element
try:
    res = function([1,2,1]*9, 12, p=10)
except IndexError as i:
    print(type(i))
    print(i)
except ValueError as v:
    print(type(v))
    print(v)
except TypeError as t:
    print(type(t))
    print(t)
except KeyError as k:
    print(type(k))
    print(k)
except ZeroDivisionError as z:
    print(type(z))
    print(z)
else:
    print("Result:", res)
finally:
    print("Thank you")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 5

### `Q-2:` You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of `sum of elements`.

List have elemnts as any no of  `key-pair dict with key as list index and value as any integer`, `integers` and `numeric-strings`. There is always only one element in the dict.


```
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])


print(s)
```

## Code Cell 6

```python
# Write code here
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    try:
        s += l[i]
    except TypeError:
        try:
            s += l[i].get(i)
        except AttributeError:
            s += int(l[i])
print(s)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

### `Q-3:`: File Handling with Exception handling

Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).

## Code Cell 8

```python
# write code here
try:
    with open("text_file.txt", "w") as f:
        f.write("Hello, Good Morning!!!")
except IOError:
    print("Error working with file...")
else:
    print("File written successfully")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 9

### `Q-4`: Number game program.

Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a **ValueTooLarge** exception. If the value is smaller the number to be guessed the, raise a **ValueTooSmall** exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise **GuessError** if user guess a number less than 1.

## Code Cell 10

```python
# Write code here
import random

class ValueTooLarge(Exception):
    def display(self):
        print("Input value is too large")

class ValueTooSmall(Exception):
    def display(self):
        print("Input value is too small")

class GuessError(Exception):
    def display(self):
        print("Guess the number between 1 and 100")

num = random.randint(1, 100)
while 1:
    try:
        guess = int(input("Enter a number:"))

        if guess < 1:
            raise GuessError

        if guess == num:
            print("Great You succeeded...")
            break
        if guess < num:
            raise ValueTooSmall
        if guess > num:
            raise ValueTooLarge
    except ValueTooSmall as s:
        s.display()
    except ValueTooLarge as l:
        l.display()
    except GuessError as g:
        g.display()

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

### `Q-5:` Cast vote

Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create **InvalidAge** exception and for name, create **InvalidName** exception. The name will be invalid when the string will be empty or name has only one word.

Example 1:

Input:

```bash
Enter the name:               goransh singh
Enter the age: 25
```

Output:

```bash
Goransh Singh  Congratulation !!! You can vote.
```

## Code Cell 12

```python
# Write code here
class InvalidAge(Exception):
    def display(self):
        print("Sorry!! Age cannot be below 18. Please come after that")
class InvalidName(Exception):
    def display(self):
        print("Please enter a valid name...")
try:
    name = input("Enter your name: ")
    if len(name) == 0 or len(name.split()) < 2:
        raise InvalidName

    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAge
except InvalidName as i:
    i.display()
except InvalidAge as a:
    a.display()
else:
    print("Your vote is accepted successfully")
finally:
    print("Thank You")
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 13

### `Q-6`: Write a python function which infinitely prints natural numbers in a single line. Raise the **StopIteration** exception after displaying first 20 numnbers to exit from the program.

## Code Cell 14

```python
# Write code here
def display(n):
    i=0
    while True:
        try:
            n+=1
            i+=1
            if i==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n, end =' ')
display(100)
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

