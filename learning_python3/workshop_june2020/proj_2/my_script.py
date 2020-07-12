"""
This is my script for doing sum of any numbers.

Usage:
    python3 my_script.py
"""


def sum_all(a,b,*args):
    """
    Returns sum of all the arguments passed to the function.

    Arguments:
        a: int
        b: int
        *arg: any number of in positional arguments

    Returns:
        Sum of all arguments
    """
    result = a+b
    for n in args:
        result+=n
    return result

def main():
    print("Hello World")
    r = sum_all(10,20,30,40)
    print(r)

print(__name__)

if __name__ == '__main__':
    main()