# Session 2

**Date**: 27-June-2020

Content
-------

## Data Types

1. Numeric - int, float
2. bool
3. None
4. str

### Numeric Types

```python
>>> a=5
>>> type(a)
<class 'int'>
>>> b=2.5
>>> type(b)
<class 'float'>
```

#### Arithmetic Operators

```python
>>> a=5
>>> b=2.0

# Addition
>>> a+b
7.0

# Subtraction
>>> a-b
3.0

# Multiplication
>>> a*b
10.0

# Division
>>> a/b
2.5

# Floor Division
>>> a//b
2.0

# Modulus
>>> a%b
1.0

# Power
>>> a**b
25.0

# divmod returns quotient and remainder 
>>> total_mins=64
>>> total_mins=65
>>> hour,min = divmod(total_mins, 60)
>>> hour
1
>>> min
5
```

#### How to explore `math` module?

```python
>>> import math

# Find all functions present in math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# Get details of a function
>>> help(math.sqrt)

```

#### Number System Conversions

How to convert between `decimal` and `binary | octal | hexadecimal`? [Click Here](NumberingSystemConversions.ipynb)

### Boolean

A boolean value can either be `True` or `False`.

```python
>>> ack=True
>>> type(ack)
<class 'bool'>
```

#### How values are treated as boolean?

```python
# Boolean Values
>>> bool(True)
True
>>> bool(False)
False

# 0 is treated False, any non-zero value is True
>>> bool(0)
False
>>> bool(1)
True
>>> bool(3)
True

# Empty string is treated False, any non-empty string is True
>>> bool("")
False
>>> bool("SomeValue")
True

# None is evaluated to False.
>>> bool(None)
False

# 'None' is str and not None, therefore evaluated to True
>>> bool('None')
True

# Empty list is evaluated to False
>>> bool([])
False
>>> bool(['book', 'pencil'])
True
```

**Q.** Write a program to take a number input from user and print if it is positive, negative or 0?

**Solution:** [numcheck.py](./numcheck.py)

Things to note,
* Taking input from stdin
* Validating input using `if`
* Terminating program using `exit`
* Type casting
* `if .. elif .. else` syntax
* f-strings

### Polymorphism (Operator Overloading Example)

The behavior of operator `+` changes based on type of operands.

* For numeric values, it does **addition**
* For string values, it does **concatenation**

```python
# Addition of Numeric values
>>> 1+2.5
3.5

# Concatenation fo String values
>>> "Tech " + "Guild"
'Tech Guild'

# If both operands are of not same type, it throws TypeError
>>> "Tech " + 2.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
```

### f-string

If you put `f` before the string, it is treated as f-string. Any value that appears betwee `{` and `}` is evaluated as expression.

```python
>>> name="Alex"
>>> age=45

# Note: I can put any expression between curly braces. E.g. {age+5}
>>> f"Hi {name}. Your age is {age}. After 5 years, you will be {age+5} years old."
'Hi Alex. Your age is 45. After 5 years, you will be 50 years old.'
```

Homework
--------

1. Write a program to take radius input from user and calculate area of a circle. [Hint: use `math.pi`]
2. Write a program to take seconds input from user. Convert it into mins and seconds and print. E.g. 125 seconds = 2 mins, 5 seconds
3. Write a program to take temprature in Fahrenheit input from user & convert it to Celcius. [Hint: You can google for conversion formula :)] 
4. Write a program to take 3 numbers input from user. Print the minimum number.
5. Refactor code in [format_time.py](format_time.py) and make it pythonic (better).

Test Cases:

```unix
$ python3 format_time.py
Enter total seconds: 5
Formatted Time = 0:05

$ python3 format_time.py
Enter total seconds: 65
Formatted Time = 1:05

$ python3 format_time.py
Enter total seconds: 130
Formatted Time = 2:10

$ python3 format_time.py
Enter total seconds: 3540
Formatted Time = 59:00

$ python3 format_time.py
Enter total seconds: 3600
Formatted Time = 1:00:00

$ python3 format_time.py
Enter total seconds: 3610
Formatted Time = 1:00:10

$ python3 format_time.py
Enter total seconds: 3660
Formatted Time = 1:01:00

$ python3 format_time.py
Enter total seconds: 3700
Formatted Time = 1:01:40
```
