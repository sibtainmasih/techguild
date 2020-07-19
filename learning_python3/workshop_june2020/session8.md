# Session 8

**Date**: 19-July-2020

Content
-------

## File Handling

* To create a file path use `os.path.join` as it makes the code platform (windows, linux, mac etc.) agnostic.

```python
>>> import os
>>> file_path= os.path.join('.', 'data', 'xyz.txt')
>>> file_path
'./data/xyz.txt'
```

* To open a file, use `open()`. It takes the path of the file to open, and returns a pointer to it.

```python
#Syntax
fp = open(file_path, mode, encoding='utf-8')
``` 

* You can `open()` a file in following modes.

| Mode | Description                                                                     |
|------|---------------------------------------------------------------------------------|
| r    | Open file in read mode. File pointer is set to beginning of the file.           |
| w    | Open file in write mode. File pointer is set to beginning of the file.          |
| a    | Open file in append mode. File pointer is set to end of the file.               |
| w+   | Open file in write and read mode. File pointer is set to beginning of the file. |
| a+   | Open file in append and read mode. File pointer is set to end of the file.      |


	* when a file is opened in write (`w` or `w+`) mode, file pointer is set to the beginning of the file.
	* when a file is opened in append (`a` or `a+`) mode, file pointer is set to the end of the file. 

* A file can be of two type. 
	1. Text `t` 
	2. Binary `b`. 

* By default the `mode` considers text file. If you want to deal with a binary file, then append `b` to the mode. E.g.
	* `wb` - open a binary file in write mode.	
	* `ab+` - Open a binary file in append and read mode.

* When writing to a file, it is important to call `fp.close()` so that content from memory gets flushed and written to the disk.

```python
fp = open(file_path, mode="w", encoding="utf-8")
fp.write( f"{content}\n")
fp.close()
```

* It is better to use `with` construct as it takes care of calling `close` function as the execution moves out of `with` block scope.

```python
with open(file_path, mode="w", encoding="utf-8") as fp:
    fp.write( f"{content}\n")
```

* `fp.write` doesn't add new line character, you have to add that explicitly for line breaks.

* When reading from a file, you can use -
	* `read(n)` - to read `n` unicode symbols  
	* `readline()` - to read a line at a time
	* `readlines()` - returns a list containing each line in the file as an element

**Note**: All the read operations will continue from current position of file pointer.

* `fp.seek(0)` sets the pointer to the beginning of the file.

```python
# Append sets the pointer to the end of file, 
# fp.seek(0) resets the pointer to the beginnig before reading file content 

with open(file_path, mode="a+", encoding="utf-8") as fp:
    fp.write( f"{content}\n")
    fp.seek(0)
    print(fp.readlines())
```

* If file doesn't exists, 
	* mode `a` or `w` creates the file. 
	* mode `r` raises `FileNotFoundError`.

## Exception Handling

### Python Philosophy - EAFP 

**E**asier to **A**sk **F**orgiveness than **P**ermission (**EAFP**) vs. **L**ook **B**efore **Y**ou **L**eap (**LBYL**). 

If you follow **LBYL**, the code will check that the file exists before reading the file.

```python
# Look Before You Leap (LBYL)
import os

if os.path.exists(file_path):
    with open(file_path, mode="r", encoding="utf-8") as fp:
        print(fp.readlines())
else:
    print(f"{file_path} does not exist.")
```

This isn't full proof method due to many reasons. For instance,

1. The file exists, but it is directory and not a text file
2. The file exists as a text file but, between the check and opening of file in `r` mode, some other process renames/deletes it.

In both the above mentioned cases, the code is goint to raise Exception.

Therefore, Python promotes EAFP i.e. _access the file first and then handle exceptions if any_.

```python
# Easier to Ask Forgiveness than Permission (EAFP).

try:
    with open(file_path, mode="r", encoding="utf-8") as fp:
        print(fp.readlines())
except FileNotFoundError as e:
    print(f"File not found. {e!r}")
```
 
### `try..except..else..finally`

* `Exception` is an event that occurs during execution of the program distrupting the normal flow. E.g.

	* `ZeroDivisionError` - Dividing a number by zero
	* `KeyError` - Accessing value for a Key which doesn't exist in a dictionary
	* `FileNotFoundError` - Opening a file to read which does not exist.
	* `IndexError` - List index out of range.

#### `try`

* `try` - Place the code that can raise exception inside `try` block.

#### `except`

* `except` - Optional. The code to handle an exception when it occurs is placed in `except` block.

* There can be multiple except blocks handling for different types of exceptions.

```python
try:
    number = ''
    for t in stmt:
        number += DIGIT_MAP[t.lower()]
    number = int(number)
    return number
except KeyError:
    print(f"The key doesn't exist: {e!r}")
    return -1
except TypeError:
    print(f"The value should be an iterable: {e!r}")
    return -1
```

* You can group multiple exceptions together, if the handling code is boilerplate.

```python
try:
    number = ''
    for t in stmt:
        number += DIGIT_MAP[t.lower()]
    number = int(number)
    return number
except (KeyError, TypeError):
    return -1
```

* To access the exception object inside `except` block use `as e`. `!r` in f-string prints e in the representation format. (`__repr__`)

```python
try:
    number = ''
    for t in stmt:
        number += DIGIT_MAP[t.lower()]
    number = int(number)
    return number
except (KeyError, TypeError) as e:
    print(f"Exception handled: {e!r}")
```

* To handle all the exceptions use `except` block.

```python
try:
    number = ''
    for t in stmt:
        number += DIGIT_MAP[t.lower()]
    number = int(number)
    return number
except (KeyError, TypeError) as e:
    print(f"Exception handled: {e!r}")
except:
    print(f"I wasn't expecting this exception. {e}")
    print("This is swallowing the exception. Don't do this!")
```

* If an exception occurs that you don't anticipate, then you can log it and then raise it again using `raise`.

```python
try:
    number = ''
    for t in stmt:
        number += DIGIT_MAP[t.lower()]
    number = int(number)
    return number
except (KeyError, TypeError) as e:
    print(f"Exception handled: {e!r}")
except Exception as e:
    print(f"I wasn't expecting this exception. {e}")
    raise
```

* You can also explicitly raise an exception from the code.

```python
raise ValueError("Age should be greater than 18 years.")
```

#### `else`

* This block is optional. 
* Code in `else` block executes when there are no exceptions in `try` block

#### `finally`

* This block is optional.
* Code in `finally` block executes regardless of any exception being raised or not raised in `try` block.
* Use this block to put code to do cleanup, e.g. If you have a database connection open, then `db.close()` will be placed in `finally` block.

[Exception Handling Example Program](./proj_3/ehe.py) 

```unix
# Execution path when there is no exception
$ python3 ehe.py 10 2
5.0
Else - Executes only when there is no exception raised in try block.
Finally - Execute in any scenario.
Program terminated gracefully.

# When there is DivisionByZero attempt then exception is handled and raised again.
$ python3 ehe.py 10 0
$ python3 ehe.py 10 0
[DEBUG]  ZeroDivisionError('division by zero')
Wide net to catch all the exceptions except ValueError. ZeroDivisionError('division by zero')
Finally - Execute in any scenario.
Program terminated gracefully.

# When they type of value is incorrect. Note that there is a return statement in except ValueError block. That's why last line of the program didn't execute but finally did.
$ python3 ehe.py 10 2.0
The value is of incorrect type. Provide integers only
Finally - Execute in any scenario.

# When the 2nd command line argument is missing
$ python3 ehe.py 10
Wide net to catch all the exceptions except ValueError. IndexError('list index out of range')
Finally - Execute in any scenario.
Program terminated gracefully.
```the o
	
Homework
--------

1. Learn how to read and write a `.csv` file. **Hint:** `import csv`

2. In [My College Project](./proj_3/mycollege) replace list storing registered students with a csv file store. A successfull add should write a record to the file. Also to view all registered students, read the all the records from file. The csv file format is -

```csv
id,name,age,subjects
1,Alice,25,Maths|History
2,Bob,26,Python|Data Science
```

```python
import csv

# Writing to csv file
with open(registration_file_path, 'a', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([1, 'Alice', 25, '|'.join(['Maths', 'History'])])
    writer.writerow([2, 'Bob', 26, '|'.join(['Python', 'Data Science'])])

# Reading from a csv file
with open(registration_file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for rec in reader:
        print(rec)
```

3. In [My College Project](./proj_3/mycollege) raise exceptions when -
	a. Admitting student with age less than 8 years.
	b. Adding student with an id which already exists.

4. In [My College Project](./proj_3/mycollege) provide a menu to the user and ask if the user wants to admit a new student or view all the admitted students. Accordingly invoke handlers. E.g.

```unix
Welcome to My College.

Please choose an action.

1. Admit a student
2. View all students
0. Quit the program
```

5. How to create a custom exception in Python? google it :)
