"""
Module to explain passing mutable objects to a function
"""

# gloabl scope
my_var=[10]


def my_fun(x):
    # local scope
    x.append(100)
    print(f"Inside Function x = {x}")


print(f"Before, my_var={my_var}")
my_fun(my_var)
print(f"After, my_var={my_var}")
