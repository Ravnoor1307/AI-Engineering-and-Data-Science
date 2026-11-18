# Study Notes: Task_05_Solutions

Generated Automatically


## Topic 1

# Tuple


## Topic 2

###`Q1:` Join Tuples if similar initial element
While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

For eg.
```
Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
```

## Code Cell 3

```python
# write your code here
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

unique = []

for i in test_list:
  unique.append(i[0])
unique = set(unique)

result = []
for i in unique:
  result.append([i])
  for j in test_list:
    if j[0] == i:
      result[-1].append(j[1])

print(list(map(tuple,result)))



```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 4

###`Q2:` Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.


For eg.
```
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication :

(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

output-(5, 40, 91, 136, 80)
```

## Code Cell 5

```python
# write your code here
t = (1, 5, 7, 8, 10)

L = []

L.append(t[0]*t[1])

for i in range(1,len(t)-1):
  L.append(t[i]*t[i-1] + t[i]*t[i+1])

L.append(t[-1]*t[-2])

print(tuple(L))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 6

###`Q3`: Check is tuples are same or not?
Two tuples would be same if both tuples have same element at same index
```
t1 = (1,2,3,0)
t2 = (0,1,2,3)

t1 and t2 are not same
```

## Code Cell 7

```python
# write your code here
t1 = (1,2,3,0)
t2 = (1,2,3,0)

flag = True
for i,j in zip(t1,t2):
  if i == j:
    continue
  else:
    flag = False
    break
if flag:
  print('same')
else:
  print('not same')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 8

###`Q4`: Count no of tuples, list and set from a list
```
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

```
`Output:`

```
List-2
Set-2
Tuples-1
```

## Code Cell 9

```python
# write your code here
L = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
output = [0,0,0]

for i in L:
  if type(i) == list:
    output[0] = output[0] + 1
  elif type(i) == set:
    output[1] = output[1] + 1
  elif type(i) == tuple:
    output[2] = output[2] + 1
  else:
    pass

print('Lists-{}\nSets-{}\nTuples-{}'.format(output[0],output[1],output[2]))


```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 10

###`Q5`: Shortlist Students for a Job role
Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

Show every students record in form of tuples if matches all required criteria.

It is assumed that there will be only one primry skill.

If no such candidate found, print `No such candidate`

`Input:`
```
Enter No of records- 2
Enter Details of student-1
Enter Student name- Manohar
Enter Higher Education- B.Tech
Enter Primary Skill- Python
Enter Year of Graduation- 2022
Enter Details of student-2
Enter Student name- Ponian
Enter Higher Education- B.Sc.
Enter Primary Skill- C++
Enter Year of Graduation- 2020

Enter Job Role Requirement
Enter Skill- Python
Enter Higher Education- B.Tech
Enter Year of Graduation- 2022
```

`Output`
```
('Manohar', 'B.tech', 'Python', '2022')
```


## Code Cell 11

```python
# write your code here
students = []

num = int(input('enter the number of applicants'))

for i in range(num):
  print('Enter details of',i+1,'applicant:')
  name = input('enter name')
  h_ed = input('enter higher education')
  p_skill = input('enter primary skill')
  yog = input('enter year of graduation')

  students.append((name,h_ed,p_skill,yog))

required_skill = input('enter required skill')
required_hed = input('enter required higher education')
required_yog = input('enter required year of graduation')

flag = False
for i in students:
  if i[1] == required_hed and i[2] == required_skill and i[3] == required_yog:
    print(i)
    flag = True

if flag == False:
  print('No such candidates')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 12

# Set

## Topic 13

###`Q1:` Write a program to find set of common elements in three lists using sets.
```
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]
```

## Code Cell 14

```python
# write your code here
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

result = list((s1 & s2) & s3)
print(result)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 15

###`Q2:` Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.

`Input:`
```
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
```
`Output:`
```
No of unique vowels-6
```

## Code Cell 16

```python
# write your code here
vowels = set('aeiouAEIOU')

s = set("hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX")

print('No of unique vowels-',len(s & vowels))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 17

### `Q3:` Write a program to Check if a given string is binary string of or not.

A string is said to be binary if it's consists of only two unique characters.

Take string input from user.

```
Input: str = "01010101010"
Output: Yes

Input: str = "1222211"
Output: Yes

Input: str = "Campusx"
Output: No
```

## Code Cell 18

```python
# write your code here
s = "010101010103"

if len(set(s)) == 2:
  print('binary')
else:
  print('not binary')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 19

### `Q4`: find union of n arrays.

**Example 1:**

Input:
```bash
[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
```

Output:

```bash
[1, 2, 3, 4, 5, 6, 7, 9]
```

## Code Cell 20

```python
# write your code here
L = [[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]

s = set()

for i in L:
  s.update(i)

print(s)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 21

### `Q5`: Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using **list-comprehension**.

**Example 1:**

Input:
```bash
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
```

Output:
```bash
[9, 10, 4, 5]
```

**Example 2:**

Input:
```bash
lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
```

Output:
```bash
[9, 11, 26, 28]
```

## Code Cell 22

```python
# write your code here
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

[item for item in lst1 if item in lst2]
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

# Dictionary

## Topic 24

### `Q1`: Key with maximum unique values

Given a dictionary with values list, extract key whose value has most unique values.

**Example 1:**

Input:

```bash
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
CampusX
```

**Example 2:**

Input:
```bash
test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
```

Output:
```bash
Best
```

## Code Cell 25

```python
# write your code here
test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}

max_val = 0
max_key = ''
for i in test_dict:
  if max_val < len(set(test_dict[i])):
    max_val = len(set(test_dict[i]))
    max_key = i

print(max_key)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 26

### `Q2`: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.

**Example 1:**

Input:

```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
```

Output:

```bash
CampusX is the best channel for Data-Science students.
```

**Example 2:**

Input:
```bash
test_str = 'CampusX best for DS students.'
repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
```

Output:
```bash
CampusX best for DS students.
```

## Code Cell 27

```python
# write your code here
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

res = []
for i in test_str.split():
  if i in repl_dict:
    res.append(repl_dict[i])
  else:
    res.append(i)

print(" ".join(res))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 28

### `Q3`: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

**Example 1:**

Input:
```bash
test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
```

Output:

```bash
[{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]
```

**Example 2:**

Input:
```bash
test_list = ["CampusX", 10]
key_list = ["name", "id"]
```

Output:

```bash
[{'name': 'CampusX', 'id': 10}]
```

## Code Cell 29

```python
# write your code here
test_list = ["CampusX", 10]
key_list = ["name", "id"]

n = len(test_list)

res = []

for i in range(0,n,2):
  res.append({key_list[0]: test_list[i],key_list[1]:test_list[i+1]})

print(res)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 30

### `Q4`: Convert a list of Tuples into Dictionary.

**Example 1:**

Input:
```bash
[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
```

Output:
```bash
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
```

**Example 2:**

Input:
```bash
[('A', 1), ('B', 2), ('C', 3)]
```

Output:
```bash
{'A': [1], 'B': [2], 'C': [3]}
```

## Code Cell 31

```python
# write your code here
L1 = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
L = [('A', 1), ('B', 2), ('C', 3)]
d = {}
for i,j in L:
  d[i] = [j]

print(d)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 32

### `Q5`: Sort Dictionary key and values List.

**Example 1:**

Input:

```bash
{'c': [3], 'b': [12, 10], 'a': [19, 4]}
```

Output:

```bash
{'a': [4, 19], 'b': [10, 12], 'c': [3]}
```

**Example 2:**

Input:

```bash
{'c': [10, 34, 3]}
```

Output:

```bash
{'c': [3, 10, 34]}
```

## Code Cell 33

```python
# write your code here

d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

res = {}

for i in sorted(d):
  res[i] = sorted(d[i])

print(res)
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

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

