# Study Notes: Week_3_Interview_Questions

Generated Automatically


## Topic 1

# Week-3

## Topic 2


###`1. What is a decorator in Python?`



## Topic 3

Python offers a unique feature called decorators.

Let's start with an analogy before getting to the technical definition of the decorators. When we mention the word "decorator", what enters your mind? Well, likely something that adds beauty to an existing object. An example is when we hang a picture frame to a wall to enhance the room.

Decorators in Python add some feature or functionality to an existing function without altering it.

Let's say we have the following simple function that takes two numbers as parameters and divides them.


```
def divide(first, second):
    print ("The result is:", first/second)
```
Now if we call this function by passing the two values 16 and 4, it will return the following output:


```
divide(16, 4)
```
The output is:

`The result is: 4.0`



## Code Cell 4

```python
def divide(first, second):
    print ("The result is:", first/second)

divide(16, 4)

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 5

What will happen if we pass the number 4 first, and 16 after? The answer will be 0.25. But we don't want it to happen. We want a scenario where if we see that first < second, we swap the numbers and divide them. But we aren't allowed to change the function.

Let's create a decorator that will take the function as a parameter. This decorator will add the swipe functionality to our function.

```
def swipe_decorator(func):
    def swipe(first, second):
        if first < second:
            first, second = second, first
        return func(first, second)

    return swipe
```

Now we have generated a decorator for the divide() function. Let's see how it works.

```
divide = swipe_decorator(divide)
divide(4, 16)
```
The output is:
```
The result is: 4.0
```

We have passed the function as a parameter to the decorator. The decorator "swiped our values" and returned the function with swiped values. After that, we invoked the returned function to generate the output as expected.



## Code Cell 6

```python
# Func refrencinf this divide function
def divide(first, second):
    print ("The result is:", first/second)

def swipe_decorator(func):
    def swipe(first, second):
        if first < second:
            first, second = second, first
        return func(first, second)
    return swipe


divide(4, 16) # Undecorated

divide = swipe_decorator(divide) # Decorated

# Decorated
divide(4, 16)
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
def divide(first, second):
    print ("The result is:", first/second)

divide(4,10) # Bigger/smaller
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
# Another way of doing the same thing

def swipe_decorator(func):
    def swipe(first, second):
        if first < second:
            first, second = second, first
        return func(first, second)
    return swipe

@swipe_decorator # divide = swipe_decorator(divide)
def divide(first, second):
    print ("The result is:", first/second)



divide(4, 16)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 10

###`2. How can you determine whether a class is a subclass of another class?`



## Topic 11

Ans:

This is accomplished by utilising a Python function called issubclass(). The function returns true or false depending on if a class is a child of another class, indicating whether it is.

## Code Cell 12

```python
class ABC:
    pass

class PQR(ABC):
    pass

print(issubclass(ABC, PQR)) # False as ABC is not the child class of PQR
print(issubclass(PQR, ABC)) # True as PQR is a child os ABC
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 13

###`3.What does Python's MRO (Method Resolution Order) mean?`




## Topic 14

Ans:

Method Resolution Order is referred to as MRO.
A class inherits from many classes under multiple inheritance.
If we attempt to access a method by building an object from the child class, the methods of the child class are first searched for the method.
If the method is not found in the child class, the inheritance classes are searched from left to right.

The `show` method is present in both the `Father` and `Mother` classes in the example presented below.

In MRO, methods and variables are searched from left to right because while conducting inheritance, `Father` class is written first and `Mother` class is written afterwards. So firstly `Father` class will be searched for `show` method if found then will get executed if not, `Mother` class will be searched.

## Code Cell 15

```python
# Example code
class Father:
  def __init__(self):
    print('You are in Father Class Constructor')

  def show(self):
    print("Father Class instance Method")

class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")

  def show(self):
    print("Mother Class instance Method")

class Son(Father, Mother):
    def __init__(self):
        print("You are in Son Class Constructor")

son = Son()
son.show()
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



## Topic 17

###`4. What’s the meaning of single and double underscores in Python variable and method names`

## Topic 18

* Single Leading Underscore: `_var`
* Single Trailing Underscore: `var_`
* Double Leading Underscore: `__var`
* Double Leading and Trailing Underscore: `__var__`
* Single Underscore: `_`

1. **Single Leading Underscore:** `_var` are a Python naming convention that indicates a name is meant for internal use. It is generally not enforced by the
Python interpreter and is only meant as a hint to the programmer.

 Adding a single underscore in front of a variable name is more like someone putting up a tiny underscore warning sign that says:

> “Hey, this isn’t really meant to be a part of the public interface of this class. Best to leave it alone.”

## Code Cell 19

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print(t.foo) #Print 11

print(t._bar) # Print 23
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 20

2. **Single Trailing Underscore:** `var_`
 Sometimes the most fitting name for a variable is already taken by a keyword in the Python language. Therefore, names like class or def cannot be used as variable names in Python. In this case, you can append a single underscore to break the naming conflict:



## Code Cell 21

```python
def make_object(name, class):
    pass
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
def make_object(name, class_):
    pass
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 23

In summary, a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords. This convention
is defined and explained in PEP 8.

## Topic 24

3. **Double Leading Underscore**: `__var`

A double underscore prefix causes the Python interpreter to rewrite
the attribute name in order to avoid naming conflicts in subclasses.

This is also called *name mangling*—the interpreter changes the name
of the variable in a way that makes it harder to create collisions when
the class is extended later.

## Code Cell 25

```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

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



## Topic 26

```
['_Test__baz', '__class__', '__delattr__', '__dict__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__',
'__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', '_bar', 'foo']
```

Let’s take this list and look for our original variable names `foo`, `_bar`, and `__baz`. I promise you’ll notice some interesting changes.

First of all, the `self.foo` variable appears unmodified as `foo` in the
attribute list.

Next up, `self._bar` behaves the same way—it shows up on the class
as `_bar`. Like I explained before, the leading underscore is just a convention
in this case—a hint for the programmer.

However, with `self.__baz` things look a little different. When you
search for `__baz` in that list, you’ll see that there is no variable with
that exact name.

So what happened to `__baz`?

> If you look closely, you’ll see there’s an attribute called `_Test__baz`
on this object. This is the name mangling that the Python interpreter
applies. It does this to protect the variable from getting overridden in
subclasses.

This type of variables also explained in `Private attributes` and `methods` session.

## Topic 27

4. **Double Leading and Trailing Underscore**: `__var__`

Double underscores `__` are often referred to as “**dunders**” in the Python
community. The reason is that double underscores appear quite often
in Python code, and to avoid fatiguing their jaw muscles, Pythonistas
often shorten “**double underscore**” to “**dunder**.”

The names that have both leading and trailing double underscores are reserved for special use in the language. This rule covers things like `__init__` for object constructors, or `__call__` to make objects callable.

These dunder methods are often referred to as magic methods.

There are many dunder methods, here are some:-

`__str__, __repr__, __call__, __add__, __sub__, __len__` etc.



## Topic 28

5. **Single Underscore** `_`:
 Sometimes used as a name for temporary or insignificant variables (“don’t care). Also, it represents the result of the last expression in a Python REPL session.


## Topic 29

### **`5. What is the difference between OOP and SOP?`**

| Object Oriented Programming | Structural Programming|
| :-- | :-- |
| Object-Oriented Programming is a type of programming which is based on objects rather than just functions and procedures | Provides logical structure to a program where programs are divided functions |
| Bottom-up approach | Top-down approach |
| Provides data hiding | Does not provide data hiding |
| Can solve problems of any complexity | Can solve moderate problems |
| Code can be reused thereby reducing redundancy | Does not support code reusability |

### **`6. Can you call the base class method without creating an instance?`**

Yes, you can call the base class without instantiating it if:
- It is a static method
- The base class is inherited by some other subclass

### **`7. What are the limitations of inheritance?`**

- Increases the time and effort required to execute a program as it requires jumping back and forth between different classes.
- The parent class and the child class get tightly coupled.
- Any modifications to the program would require changes both in the parent as well as the child class
- Needs careful implementation else would lead to incorrect results

### **`8. What is the difference between range() and xrange()?`**

- range() creates a static list that can be iterated through while checking some conditions. This is a function that returns a list with integer sequences.
- xrange() is same in functionality as range() but it does not return a list, instead it returns an object of xrange(). xrange() is used in generators for yielding.

| range() | xrange() |
| :-- | :-- |
| In Python 3, xrange() is not supported; instead, the range() function is used to iterate in for loops. | The xrange() function is used in Python 2 to iterate in for loops.
| It returns a list. | It returns a generator object as it doesn’t really generate a static list at the run time. |
| It takes more memory as it keeps the entire list of iterating numbers in memory. | It takes less memory as it keeps only one number at a time in memory. |

## Topic 30

### **`9. How to override the way objects are printed?`**

Use the `__str__` and the `__repr__` dunder methods.

Here’s an example that demonstrates how an instance from the Person class can be nicely formatted when printed to the console.

## Code Cell 31

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

person = Person("John", "Doe", 30) # thanks to __str__
person
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 32

### **`10. What is the difference between a class method, a static method and an instance method?`**



## Topic 33

Let’s begin by writing a (Python 3) class that contains simple examples
for all three method types:
```
class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

**`Instance Methods`**

The first method on `MyClass`, called `method`, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called. But of course, instance methods can accept more than just one parameter.

Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the `self.__class__` attribute. This means instance methods can also modify class state.  This makes instance methods powerful in terms of access restrictions—they can freely modify state on the object instance and on the class itself.




## Topic 34

**`Class Methods`**

Let’s compare that to the second method, `MyClass.classmethod`. I marked this method with a [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator to flag it as a class method. Instead of accepting a self parameter, class methods take a `cls` parameter that points to the class—and *not* the object instance—when the method is called.

Since the class method only has access to this `cls` argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

## Topic 35

`Static Methods`

The third method, `MyClass.staticmethod` was marked with a [`@staticmethod6`](https://docs.python.org/3/library/functions.html#staticmethod) decorator to flag it as a static method.

This type of method doesn’t take a `self` or a `cls` parameter, although, of course, it can be made to accept an arbitrary number of other parameters.

As a result, a static method cannot modify object state or class state.
Static methods are restricted in what data they can access—they’re primarily a way to namespace your methods.

## Topic 36

**Let’s See Them in Action!**

Let’s take a look at how these methods behave in action when we call them. We’ll start by creating an instance of the class and then calling the three different methods on it.

`MyClass` was set up in such a way that each method’s implementation returns a tuple containing information we can use to trace what’s going on and which parts of the class or object that method can access.


## Code Cell 37

```python
# Class

class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 38

Here’s what happens when we call an instance method:

## Code Cell 39

```python
obj = MyClass()
obj.method()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 40

This confirms that, in this case, the instance method called method has access to the object instance (printed as `<MyClass instance>`) via the self argument.

When the method is called, Python replaces the `self` argument with the instance object, `obj`.

We could ignore the syntactic sugar provided by the `obj.method()` **dot-call syntax** and pass the instance object manually to get the same result:
```
MyClass.method(obj)
```


## Code Cell 41

```python
MyClass.method(obj)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Code Cell 42

```python
type(obj)
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 43

Let’s try out the **class method** next:


## Code Cell 44

```python
obj.classmethod()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 45

Calling `classmethod()` showed us that it doesn’t have access to the `<MyClass instance>` object, but only to the `<class MyClass>` object, representing the class itself (**everything in Python is an object, even classes themselves**).

Notice how Python automatically passes the class as the first argument to the function when we call `MyClass.classmethod()`. Calling a method in Python through the **dot syntax** triggers this behavior. The `self` parameter on instance methods works the same way.

Please note that naming these parameters `self` and `cls` is just a convention. You could just as easily name them `the_object` and `the_class` and get the same result. All that matters is that they’re positioned first in the parameter list for that particular method.

## Topic 46

Time to call the **static method** now:


## Code Cell 47

```python
obj.staticmethod()
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 48

Did you see how we called `staticmethod()` on the object and were able to do so successfully? Some developers are surprised when they learn that it’s possible to call a static method on an object instance.

Behind the scenes, Python simply enforces the access restrictions by
not passing in the `self` or the `cls` argument when a static method gets
called using the dot syntax

This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’ (and every instance’s) namespace.

Now, let’s take a look at what happens when we attempt to call these
methods on the class itself, **without creating an object instance** beforehand:

## Code Cell 49

```python
# Class Method
print(MyClass.classmethod())
# Static method
print(MyClass.staticmethod())
#Instance Method
print(MyClass.method())
```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises



## Topic 50

We were able to call `classmethod()` and `staticmethod(`) just fine, but attempting to call the instance method `method()` failed with a `TypeError`.

This is to be expected. This time we didn’t create an object instance and tried calling an instance function directly on the class blueprint itself. This means there is no way for Python to populate the `self` argument and therefore the call fails with a `TypeError exception`.

This should make the distinction between these three method types a
little more clear

## Topic 51

**Key Takeaways**
* Instance methods need a class instance and can access the instance through `self`.
* Class methods don’t need a class instance. They can’t access the
instance (`self`) but they have access to the class itself via `cls`.
* Static methods don’t have access to `cls or self`. They work like
regular functions but belong to the class’ namespace.
* Static and class methods communicate and (to a certain degree)
enforce developer intent about class design. This can have definite maintenance benefits.


## Code Cell 52

```python

```

### Things To Learn

- Purpose of this code
- Concepts involved
- Expected output
- Common mistakes
- Interview questions
- Practice exercises

