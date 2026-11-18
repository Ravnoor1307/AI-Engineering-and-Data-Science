# Study Notes: week3_interview_questions

Generated Automatically


## Topic 1

- How indexing works in sets
- Why dict key cant be mutable data types
- Enumerate
- destructor
- dir/isinstance/issubclass
- classmethod vs staticmethod
- The diamond problem
- What’s the meaning of single and double underscores in Python variable and method names
- Magic Methods (repr vs str)
- How can objects be stored in sets even though they are mutable

## Code Cell 2

```python
s = {21,34,11,56,39}
s
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
d = {(1,2,3):'nitish'}
d
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
d = {[1,2,3]:'nitish'}
d
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
# enumerate
# The enumerate() method adds a counter to an iterable and returns it (the enumerate object).
L = [('nitish',45),('ankit',31),('ankita',40)]

sorted(L,key=lambda x:x[1],reverse=True)
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
L = [15,21,13,13]
sorted(list(enumerate(L)),reverse=True)
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
# destructor
class Example:

  def __init__(self):
    print('constructor called')

  # destructor
  def __del__(self):
    print('destructor called')

obj = Example()
a = obj
del obj
del a
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
# dir

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

    def greet(self):
      print('hello')

t = Test()
print(dir(t)) # This gives us a list with the object’s attributes
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
# isinstance

class Example:

  def __init__(self):
    print('hello')

obj = Example()

isinstance(obj,Example)
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
# issubclass
class A:
  def __init__(self):
    pass

class B(A):
  pass

issubclass(B,A)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 11

### classmethod
- A class method is a method that is bound to the class and not the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
- It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.

## Topic 12

### staticmethod
A static method does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

## Code Cell 13

```python
class A:

  def normal_m(self):
    print('normal method')

  @staticmethod
  def static_m():
    print('static method')

  @classmethod
  def class_m(cls):
    print('class method')
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
a = A()

# normal -> object -> callable
a.normal_m()
# class -> object -> callable
a.class_m()
# static -> object -> not callable
a.static_m()
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
# static -> class -> callable
A.static_m()
# class method -> class -> callable
A.class_m()
# normal -> class -> not callable
A.normal_m()
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
# Alternate syntax
A.normal_m(a)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 17

### Class method vs Static Method<br>
The difference between the Class method and the static method is:

- A class method takes cls as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

## Topic 18

### When to use the class or static method?
- We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
- We generally use static methods to create utility functions.

## Code Cell 19

```python
# The diamond problem
class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class3, Class2):
    pass

obj = Class4()
obj.m()
# MRO
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 20

```python
# Double and single score
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
# repr and other magic/dunder methods

a = 'hello'

print(str(a))
print(repr(a))
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
import datetime

a = datetime.datetime.now()
b = str(a)

print(str(a))
print(str(b))

print(repr(a))
print(repr(b))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

### In summary

- str is for users -> meant to be more readable
- repr is for developers for debugging - > for being unambigous

## Code Cell 24

```python
# how objects are stored even though they are mutable
# https://stackoverflow.com/questions/31340756/python-why-can-i-put-mutable-object-in-a-dict-or-set
class A:

  def __init__(self):
    print('constructor')

  def hello(self):
    print('hello')

a = A()
a.hello()
s = {a}
print(s)
dir(a)
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
class A:

  def __init__(self):
    print('constructor')

  def __eq__(self):
    pass

  def __hash__(self):
    return 1

  def hello(self):
    print('hello')

a = A()
a.hello()
s = {a}
print(s)

dir(a)


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
class A:

  def __init__(self):
    self._var = 10

a = A()
a._var
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
s = {[1,2]}
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
L = [1,2,3]
s = {L}
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
print(L.__hash__)
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
hash(1)
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
hash('hello')
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 32

```python
hash((1,2,3,))
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 33

```python
hash([1,2,3])
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

