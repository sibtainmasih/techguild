# Session 6

**Date**: 11,12-July-2020

Content
-------

## Modularity

### Function

* Creating function with `def` keyword

```python
#  No argument, no return value
def greeting():
    print("Hello Student")

# An argument, but no return value
def launch_missile(count):
    print(f"{count} misslies launched.")
```

* Calling / invoking a function

```python
>>> greeting()
Hello Student
>>> launch_missile(5)
5 misslies launched.
```

* Return a value from a function using `return` keyword

```python
def square(n):
    sq = n**2
    return sq

# Calling square function
>>> res = square(6)
>>> res
36
```

* Return multiple values from a function

```python
def sq_cube(n):
    sq = n**2
    cb = n**3
    return sq, cb

# Calling sq_cube function
>>> s,c = sq_cube(5)
>>> s
25
>>> c
125
```

* In reality, returning multiple values from a function is just syntactic sugar. Python just packs them in a tuple and returns a single tuple.

```python
>>> t = sq_cube(3)
>>> t
(9, 27)
>>> type(t)
<class 'tuple'>

# Here due to tuple unpacking value of square is stored in s and value of cube is stored in c.
>>> s,c = sq_cube(5)
>>> s
25
>>> c
125
```

* A function can take zero or more arguments.

```python
def print_vector(x, y, z):
    print(f"Vector is: x={x}, y={y}, z={z}")

# Function call
>>> print_vector(10,30,90)
Vector is: h=10, x=30, y=90, z=10

>>> print_vector(y=6,z=13,x=9)
Vector is: x=9, y=6, z=13
```

* You can specify default values for function parameters. E.g. default value for `z` in `10`

```python
def print_vector(x, y, z=10):
    print(f"Vector is: x={x}, y={y}, z={z}")


# Function is called with just values of x and y, z is set to default
>>> print_vector(1,2)
Vector is: x=1, y=2, z=10

# If value for z is passed then -
>>> print_vector(1,2,3)
Vector is: x=1, y=2, z=3
```

**Note:** Non-default arguments come first and then aguments with default values

* Unpacking a tuple and passing it as argument using `*`

```python
def print_vector(x, y, z=10):
    print(f"Vector is: x={x}, y={y}, z={z}")

# Passing a tuple as argument 
>>> vt = 10,5,6
>>> print_vector(*vt)
Vector is: x=10, y=5, z=6

# Passing tuple with 2 values
>>> vt = 10,5

>>> print_vector(*vt)
Vector is: x=10, y=5, z=10

# Specifying value for z in function call
>>> print_vector(*vt,70)
Vector is: x=10, y=5, z=70

# If you provide first postitional argument, it is mapped to x and the values in tuple are mapped to y and z.
>>> print_vector(12, *vt)
Vector is: x=12, y=10, z=5
```

* Passing a dictionary as argument to a function using `**`

```python
>>> vd = {'y':80, 'x': 9}
>>> print_vector(**vd)
Vector is: x=9, y=80, z=10

>>> vd = {'y':80, 'z': 50, 'x': 9}
>>> print_vector(**vd)
Vector is: x=9, y=80, z=50

# Not allowed as value x is passed via positional arg and now again appearing in dict as key 'x'
>>> vd = {'x':9, 'z': 12}
>>> print_vector(6,**vd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_vector() got multiple values for argument 'x'
```
**Note**: The keys in the dictionary should be same as names of arguments of the function to which it is passed using `**`.

* The order is important - first any positional, then `*` and then `**` in function call.

```python
def print_vector(h, x, y, z=10):
    print(f"Vector is: h={h}, x={x}, y={y}, z={z}")

# Calling function and passing positional, tuple and dict arguments
>>> vt=12,13
>>> vd={'z':99}
>>> print_vector(11,*vt,**vd)
Vector is: h=11, x=12, y=13, z=99
```

* `*args` and `**kwargs` in function definition

```python
def my_sum(a,b,*args,**kwargs):
    print(f"a = {a}, {type(a)}")
    print(f"b = {b}, {type(b)}")
    print(f"args = {args}, {type(args)}")
    print(f"kwargs = {kwargs}, {type(kwargs)}")

# Output
>>> my_sum(10,20)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (), <class 'tuple'>
kwargs = {}, <class 'dict'>

>>> my_sum(10,20,30)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (30,), <class 'tuple'>
kwargs = {}, <class 'dict'>

>>> my_sum(10,20,30,40)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (30, 40), <class 'tuple'>
kwargs = {}, <class 'dict'>

>>> my_sum(10,20,30,40,x=100)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (30, 40), <class 'tuple'>
kwargs = {'x': 100}, <class 'dict'>

>>> my_sum(10,20,30,40,x=100,y=200)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (30, 40), <class 'tuple'>
kwargs = {'x': 100, 'y': 200}, <class 'dict'>

>>> my_sum(10,20,x=100,y=200)
a = 10, <class 'int'>
b = 20, <class 'int'>
args = (), <class 'tuple'>
kwargs = {'x': 100, 'y': 200}, <class 'dict'>
```

**Q.** Write a function that take any number of arguments (minimum 2) and returns sum of all the values.

```python
def sum_all(a,b,*args):
    result = a+b
    for n in args:
        result+=n
    return result
```

### Module

* A file with `.py` extension is a Python module.

```python
# my_script.py
def main():
    print("Hello World")

if __name__ == '__main__':
    main()
```

* A module contains Python code - variables, functions, classes, statements etc.
* You can import functions from a module in different ways. E.g. [my_math.py](./proj_2/my_math.py)

```python
# 1 - import a module
>>> import my_math
>>> my_math.sq_cube(4)
(16, 64)

# 2 - Import a specific function from a module
>>> from my_math import sq_cube
>>> sq_cube(5)
(25, 125)

# 3 - Import multiple functions from a module
>>>>> from my_math import sq_cube, print_vector

# 4 - Import everthing from a moduel [NOT RECOMMENDED]
>>> from my_math import *

# 5 - Import a function from a module and access it using alias to avoid namespace conflicts
>>> from my_math import print_vector as pvector
>>> pvector(90,22,39,100)
Vector is: h=90, x=22, y=39, z=100
```

#### What is `__name__`?

* You can -
	* execute a python module - `python3 my_script.py` or 
	* import a module into another `import my_script`.
* `__name__` is a special member of any python module.
* Python sets value of `__name__` to -
	* `__main__` when the module is executed directly.
	* name of the module when it is imported it in another module.
* If you want to execute code when the module is directly invoked, then place that code within `if __name__ == '__main__':` block.

```python
# new_script.py

print(__name__)

if __name__ == '__main__':
    print("Module is directly invoked.")
```

When new_script.py is invoked directly -

```unix
# Value of __name__ is __main__
$ python3 new_script.py 
__main__
Module is directly invoked.
```

When new_script is imported as module -

```python
# Value of __name__ is module name i.e. new_script
>>> import new_script
new_script
>>> 
```

#### Scope

* The scope for variable defined in a module is `global`. 
* The scope for variable defined in a function is `local`.
* Global vs. Local Scope - [Click Here](scope1.py)

```python
# Output
Before, my_var=10
Inside Function my_var = 100
After, my_var=10
``` 

* If you **pass mutable objects to a function** as argument - though they are modified in local scope (inside function), the change also is visible in global scope. For example, [Click Here](scope2.py)

```python
# Output
Before, my_var=[10]
Inside Function x = [10, 100]
After, my_var=[10, 100]
```

* If you want to modify gloabl variable in a local scope, use `global` keyword. [Click Here](scope3.py) for example. **NOT RECOMMENDED**

```python3
# Output
Before, my_var=10
Inside Function my_var = 110
After, my_var=110
```

#### Docstring

* Docstring provides details of the module and functions defined inside the module.
* This is used when `help()` function is called.
* Use `"""` at the top of a `.py` file to describe the module and how to use it.
* Use `"""` at the top of each function definition to describe what functions does, what all arguments it takes and what it returns.
* For example, [Click Here](./proj_2/my_script.py)

```python
>>> import my_script
>>> help(my_script)

Help on module my_script:

NAME
    my_script - This is my script for doing sum of any numbers.

DESCRIPTION
    Usage:
        python3 my_script.py

FUNCTIONS
    main()
    
    sum_all(a, b, *args)
        Returns sum of all the arguments passed to the function.
        
        Arguments:
            a: int
            b: int
            *arg: any number of in positional arguments
        
        Returns:
            Sum of all arguments
```


Homework
--------

1. Write a function to check if a number is prime or composite.

