# Session 10

**Date**: 08,09-Aug-2020

Content
-------

## String Formating Flavors

```python
name = "Alex"
salary  = 1235.88893

# 1. String Concatenation (+)
print ('Hello ' + name + ", You earn " + str(salary) )

# 2. C style formating
print('Hello, %s, You earn %.2f' % (name, salary))

# 3. Using .format

# 3.1 Positional Arguments
print("Hello, {0}. You earn {1:.2f}. Hey! {0} do you want hike?".format(name, salary))

# 3.2 Keyword Arguments
print("Hello {n}. You earn {s:.3f}. Hey! {n} do you want hike?".format(n=name, s=salary))

# Passing a dictionary to .format
values = dict(n="James", s=123.456789)
print("Hello {n}. You earn {s:.3f}. Hey! {n} do you want hike?".format(**values))

# 4. Using f-string (recommended)
# print (f"Hello {name}, You earn {salary:.2f}.")
```

## Emulate Switch case functionality in Python
	
There is switch-case control structure in Python. This functionality can be achieved using - 

* dict keys as cases to match
* value for each key will be a reference to a function
* the function body will have code to be executed when a case is matched

[Click Here](https://www.youtube.com/watch?v=hf4aZCMU3og) for a 10 mins video tutorial on YouTube.

```python
def one():
    return "ONE"

def two():
    return "TWO"

def default_action():
    return "Incorrect Value"

fun_dict = {1: one, 2: two}
print(fun_dict)

x = int(input("Enter a number: "))
f = fun_dict.get(x, default_action)
print(f())
```

## Tour of Python Standary Library

### re

To use regular expression based tasks, use **re** module.

```python
# Extract all the numbers from a string.
import re


s = '100klh564abc365bg'
p = re.compile('\d+')
result = p.findall(s)
print(result)
```

### datetime and pytz

* `datetime` is used to deal with date and time values in Python.
* By deafult `datetime` objects are not time zone aware.
* To set time zone or to convert a datetime value between time zones use `pytz`.

**Note:** In real world applications, it is recommended to store datetime values in `UTC` timezone.

```python
# Creating datetime objects

>>> from datetime import datetime

>>> now = datetime.now()
>>> print(now)
2020-08-09 12:43:51.805871

>>> utcnow = datetime.utcnow()
>>> print(utcnow)
2020-08-09 07:14:09.357901

>>> d = datetime(2010, 12, 6, 14, 5)
>>> print(d)
2010-12-06 14:05:00

# Usefult attributes and methods of date object -> dir(now)

>>> now.weekday()
6
>>> now.year
2020
>>> now.month
8
>>> now.date()
datetime.date(2020, 8, 9)
>>> now.time()
datetime.time(12, 43, 51, 805871)

# String Formating of date object
>>> datetime.strftime(d, '%d-%B-%Y')
'06-December-2010'

# Parsing a string into a datetime object
>>> datetime.strptime("December 25, 2010", "%B %d, %Y")
datetime.datetime(2010, 12, 25, 0, 0)

# By defaults, dateetime objects are not timezone aware
>>> print(utcnow.tzinfo)
None

# Set timezone to utc
>>> import pytz
>>> utcnow = pytz.utc.localize(datetime.utcnow())
>>> print(utcnow)
2020-08-09 07:22:15.006394+00:00

# Convert between timezones
>>> istnow = utcnow.astimezone(pytz.timezone("Asia/Kolkata"))
>>> print(istnow)
2020-08-09 12:52:15.006394+05:30
```

### logging

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(name)s][%(asctime)s][%(levelname)s] - %(message)s",    
    filename="app.log",
    filemode="a"
)

logger = logging.getLogger(__name__)

# Log Levels
logger.debug("This is a debug message.")
logger.info("This is information.")
logger.warning("Warning message.")
logger.error("Some error occured message.")
logger.critical("Critical. After this application will stop.")

try:
    res = 10/0
except ZeroDivisionError:
    logger.exception("Error occured while dividing numbers.")
```

### argparse

```python
"""
This program shows how to take path of a log file from command line and identify all CRITICAL logging statements.
"""
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="This is a log actioner.")
    parser.add_argument(
        '-f',
        action="store",
        help = "Path of log file",
        type=str,
        required=True
    )

    return parser

def read_log_file(file_path):
    with open(file_path, mode="r") as f:
        return [ 
            line  
            for line in f.readlines() 
            if 'Critical'.lower() in line.lower()  
        ]


if __name__ == "__main__":
    my_parser = get_parser()
    args = my_parser.parse_args()
    file_path = args.f
    data = read_log_file(file_path)
    print(data)
```


Homework
--------

1. Learn regular expressions and implment using re module.
2. Expore datetime and pytz module.
3. Instead of print use, start using logging in your application.
4. Write a calculator program to take numbers and operations input from command line. Log the activities in the application. Also control the logging level from commandline.
