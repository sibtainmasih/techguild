# Session 1

**Date**: 20 & 21-June-2020

Content
-------

### Introduction

* Python is **interpreted**.
* In Python, you have to decalre and define variable at the same time.

```python
>>> marks=76
>>> marks
76

>>> x=y=20
>>> x
20
>>> y
20

>>> name, age = "Alex", 26
>>> name
'Alex'
>>> age
26

>>> name, *marks, percentage = "Alex", 26, 50, 67,  76.61
>>> name
'Alex'
>>> marks
[26, 50, 67]
>>> percentage
76.61
```

* Python is **dynamically typed language**.
* The type of the variable is automatically determined at runtime based on the type of value assigned.

```python
>>> name, age, percentage = "Alex", 26, 76.61
>>> type(name)
<class 'str'>
>>> type(age)
<class 'int'>
>>> type(percentage)
<class 'float'>
```

* The type of a variable can change if the type of value assigned changes. 

```python
>>> a=10
>>> type(a)
<class 'int'>
>>> a="Alex"
>>> type(a)
<class 'str'>
```

* Everything in Python is object. 
* Everything is stored in heap.
* Everything is by ref and there is no by val.
* `id` function can be used to get identity of the object. (Think of it as memory location address)
* Integers are specially treated in Python, making it efficient for number crunching.

```python
>>> a=1
>>> id(a)
11259008
>>> b=2
>>> id(b)
11259040
>>> b=b-1
>>> id(b)
11259008
```

### Writing first Python program

**Q.** Write a program to ask user for name and print a greeting message?

**Solution:** [greet.py](./greet.py)

Note:

* Make the file executable - `chmod u+x greet.py`
* The first line is [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) which tells the interpreter to use.
* Execute the program as `./greet.py`

### String

* String can be create with single or double quotes.
* Multiline string can be created using **triple** quotes.

```python
>>> first_name = "Faizan"
>>> last_name = 'Khan'
>>> msg = """
... This is line 1 of message.
... This is line 2 of message.
... And this is last line.
... """
```

* String is **immutable** sequence of characters.

Note:
* Mutable = Value of an object changes but it's `id` **does not** change.
* Immutable = If the value of object changes and its `id` also changes.

```python
>>> message = "Alex."
>>> message
'Alex'
>>> id(message)
139629172839232
>>> message = "Hello " + message
>>> message
'Hello Alex.'
>>> id(message)
139629172828464
```

* Use `len()` function to get string length.

```python
>>> name="Asjad"
>>> len(name)
5
```

* Use `+` for string concatenation and `*` for repitition.

```python
# Concatenation
>>> message = "Alex."
>>> message
'Alex'
>>> message = "Hello " + message
>>> message
'Hello Alex.'

# Repition - Useful for creating banners in commandline programs
>>> "="*15
'==============='
```

* String slicing - `[start:stop:step]`
* `start`, `stop` and `step` - all are optional.
* Default values -
	* `start` = 0.
	* `stop`  = end of string.
	* `step`  = 1.
* **Negative indexing** is allowed.
* Hint: Any operation you want to peform from end of string, use negative index.

```python
>>> x="ABCDEFG"

# Get character at index = 0
>>> x[0]
'A'

# Get 2nd character
>>> x[1]
'B'

# Get 4th character
>>> x[3]
'D'

# Get last character
>>> x[-1]
'G'

# Get 2nd last character
>>> x[-2]
'F'

# Get all the characters starting from index 3
>>> x[3:]
'DEFG'

# Get first 3 characters
>>> x[:3]
'ABC'

# Get last 3 characters
>>> x[-3:]
'EFG'

# Get 3 characters from index 2
>>> x[2:5]
'CDE'

# Get clone of the string
>>> x[:]
'ABCDEFG'

# Get all the characters at even index position
>>> x[::2]
'ACEG'

# Get all the characters at odd index position
>> >>> x[1::2]
'BDF'

>>> x[::-1]
'GFEDCBA'
```

* `in` is called **membership** operator. It is used to check for *substring*.
* It returns `True` if substrig is present, `False` otherwise.

```python
>>> sentence="It is raining in Mumbai."
>>> "is" in sentence
True
>>> "rain" in sentence
True
>>> "Delhi" in sentence
False
```

* How to find methods supported by string? `dir`
* **Note:** Attributes or methods starting with `__` (called **dunder**) are internal to Python.

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

* How to get help for any method? `help`

```python
>>> help(str.replace)
```

Home Work
----------

1. Write a program to take a sentence input from user and check if it is **palindrome**?
2. Write a program to take a character input from user and check it is vowel or consontant?
3. Write a program to take 2 numbers input from user and print their sum and product?






