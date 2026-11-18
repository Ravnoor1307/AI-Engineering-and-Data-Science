# Study Notes: Task_11

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



## Code Cell 6

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 7

###`Q-2:` You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of `sum of elements`.

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

## Code Cell 8

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



## Topic 9

### `Q-3:`: File Handling with Exception handling

Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).

## Code Cell 10

```python
# write code here
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

### `Q-4`: Number game program.

Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a **ValueTooLarge** exception. If the value is smaller the number to be guessed the, raise a **ValueTooSmall** exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise **GuessError** if user guess a number less than 1.

## Code Cell 12

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



## Topic 13

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

## Code Cell 14

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



## Topic 15

### `Q-6`: Write a python function which infinitely prints natural numbers in a single line. Raise the **StopIteration** exception after displaying first 20 numnbers to exit from the program.

## Code Cell 16

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

