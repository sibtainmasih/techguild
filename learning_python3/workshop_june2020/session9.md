# Session 9

**Date**: 25,26-July-2020

Content
-------

## File Handling (continue...)

### Reading and writing to a csv file

* Readinig records from a csv file

```python
def _fetch():
    """
    Returns a list of records fetched from the backend store.
    """
    records = []

    with open(FILE_STORAGE_PATH, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for rec in reader:
            rec['is_junior'] = True if int(rec['age'])>=18 else False
            records.append(rec) 

    return records
```

* Writing records to a csv file

```python
def _save(student_obj):
    """
    Saves student record in the backend store.
    """
    with open(FILE_STORAGE_PATH, mode="a", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=student_obj.keys())
        writer.writerow(student_obj)
```

## Python Debugger (pdb)

[Click Here](https://www.youtube.com/watch?v=5AYIe-3cD-s) for a PyCon video on pdb.

The code used to explain pdb - [debugexample.py](./proj_3/debugexample.py)

* Add `breakpoint()` to the code. (Don't check-in code with breakpoints)

```python
def get_student(stud_id):
    breakpoint()
    for stud in _fetch():
        if stud_id == stud['id']:
            return stud
```

* Useful PDB commands

| Command         | Description                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------|
| `n`             | **n**ext line                                                                                            |
| `s`             | **s**tep into a function call                                                                            |
| `r`             | continue till **r**eturn statement of a function                                                         |
| `__return__`    | Print the return value when you have reached the end of the function                                     |
| `c`             | **c**ontinue execution till next breakpoint()                                                            |
| `j <n>`         | **j**ump to a line number; useful to break out of a loop                                                 |
| `l`             | print next 11 **l**ines from current debug point, if you enter l again, it will print previous 11 lines. |
| `l .`           | reset l to the top of the file                                                                           |
| `ll`            | **l**ong **l**ist to see the function you are currently in                                               |
| `a`             | Print **a**ll the arguments to a function                                                                |
| `p`             | **p**rint value of a variable / expression                                                               |
| `pp`            | **p**retty **p**rint value of a variable / expression                                                    |
| `w`             | Print the call stack                                                                                     |
| `b`             | Show all **b**reakpoints                                                                                 |
| `b <n>`         | Set a breakpoint on a line number                                                                        |
| `disable <bpn>` | Disable a breakpoint, and breakpoint number (bpn) is provided by `b`.                                    |
| `enable <bpn>`  | Enable a breakpoint                                                                                      |
| `cl`            | **cl**ear all breakpoints                                                                                |
| `interact`      | Open a Python REPL, press `ctrl+D` to exit                                                               |
| `h`             | **h**elp                                                                                                 |
| `q`             | **q**uit                                                                                                 |

**Note:** Just press `ENTER` to execute the last command you punched in.

* If you set environment variable `PYTHONBREAKPOINT=0` then breakpoints in the program wiill be ignored.

* If you can't modify the code to add `breakpoint()` then to run with pdb & add breakpoint on a line -

```unix
$ python -m pdb mycollege/app.py 

Pdb) l
  1  -> from mycollege.views import student
  2  
  3     def main():
  4         print("Welcome to My College!")
  5         student.display_all()
  6         try:
  7             student.add(2, 'Faizan', 25, ['Python'])
  8             student.add(3, 'Imran', 7, ['Math', 'Music'])
  9         except ValueError as e:
 10             print(f"{e!r}")
 11  
 
Pdb) b 8
Breakpoint 1 at /home/sibtain/work/techguild/learning_python3/workshop_june2020/proj_3/mycollege/app.py:8

(Pdb) c
> /home/sibtain/work/techguild/learning_python3/workshop_june2020/proj_3/mycollege/app.py(8)main()
-> student.add(3, 'Imran', 7, ['Math', 'Music'])

(Pdb) s
--Call--
> /home/sibtain/work/techguild/learning_python3/workshop_june2020/proj_3/mycollege/mycollege/views/student.py(4)add()
-> def add(stud_id, name, age, subjects):
```

* pdb shows `student.py(4)add()` as it's current position whiich is in the form `module(line_number)fn_name()`.

* Don't leave `breakpoint()` in code when you check-in. **Tip:** Use pre-commit hook in git to enforce this.	

## Installing External Packages

One time setup on Ubuntu -

```unix
sudo apt install python3-pip
apt-get install python3-venv
```

### Create Virtual Environment & Install Packages

1. Create a virtual (sandbox) environment.

```unix
$ python3 -m venv ~/.pyvenv/techguild
```

2. Activate a virtual environment

```unix
$ . ~/.pyvenv/techguild/bin/activate

# Below prompt indicates "techguild" is the active virtual environment.
(techguild) sibtain@sibtain-HP-Compaq:/tmp$
```

3. Install a package

```unix
$ pip install flask
```

4. Deactivate a virtual environment

```unix
$ deactivate
```

## Python Powerful Tools

1. Pylint - Python code linter

```unix
$ pip install pylint
$ pylint my_proj/
```

2. Black - Opinionated code formating. (Some one called it #BeautyParlour for code)

```unix
$ black my_proj/
```

3. Bandit - Security Vulenrabilities

```unix
$ bandit -r my_proj/
```
	
Homework
--------

1. Play with **pdb**.
2. Learn about different options **pip** command supports. E.g. search, list, freeze.
3. Learn about different configuration options for **pylint**, **black** and **bandit**.
4. Work on [Code Refactoring Examples](./refactor_exercises).
