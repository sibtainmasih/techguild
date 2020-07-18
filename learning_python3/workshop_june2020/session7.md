# Session 7

**Date**: 18-July-2020

Content
-------

## Modularity (continue...)

### Module

* The code in the module gets executed only once - when the module is imported for the first time. [myprog.py](./proj_3/myprog.py)

```python
# myprog.py
import sys

def banner(msg, symbol="#"):
    line = len(msg) * symbol
    print(line)
    print(msg)
    print(line)

def main():
    print("Hello World")
    banner("Tech Guild", symbol='*')

main()


# When module is imported 
>>> import myprog
myprog
Hello World
**********
Tech Guild
**********
>>> import myprog  # Now I am importing module again, but the code isn't executing.
>>> import myprog
```

* You can use `__main__.py` to specify entry point to a Python project. [myprog](./proj_3/myprog)

```unix
$ tree myprog
myprog
`-- __main__.py

$ cat myprog/__main__.py 
print("Hello, this is example of specifying entry point using __main__.py")

$ python3 myprog
Hello, this is example of specifying entry point using __main__.py
```

* Accepting commandline arguments using `sys.argv`

```python
# mycmd.py
import sys
print(sys.argv)

#Output
$ python3 mycmd.py 'Alice' 56 India
['mycmd.py', 'Alice', '56', 'India']
```

### Package

* A package is a directory which contains one or more modules. It can also contain other packages.

```unix
# mycollege is a package which contains models, views and controllers, these 3 packages.
# views is a package which contains student and utils modules.

$ tree mycollege/
mycollege/
|-- controllers
|   |-- __init__.py
|   `-- student.py
|-- __init__.py
|-- models
|   |-- __init__.py
|   `-- student.py
`-- views
    |-- __init__.py
    |-- student.py
    `-- utils.py
```


* A package also contains a special module file `__init__.py`. Here usually you don't put any code, instead any imports that you want to expose at package level.

```python
from mycollege.views.student import get_student
```

Instead of this, if I add following line in `views/__init__.py`

```python
from .student import get_student
```

then in any other module, I can import it directly from package itself as -

```python
from mycollege.views import get_student
```

* You also do relative imports usin `.` or `..`.

```python
$ cat mycollege/views/student.py 
from .utils import banner
```

* Module import ordering good practice -
	1. import Python standard library modules first. E.g. `sys`, `os`
	2. then import any third party packages. E.g. `flask`, `django`
	3. at the end import packages/modules created in your project. 

* Model-View-Controller (MVC) Project Structure - [My College Project](./proj_3/mycollege)

Homework
--------

1. Think of a website theme and structure your project using MVC patterns. E.g. [My College Project](./proj_3/mycollege)
