"""
Module to explain scope of variables
"""

# gloabl scope
my_var=10


def my_fun(x):
    # local scope
    my_var = x
    print(f"Inside Function my_var = {my_var}")


print(f"Before, my_var={my_var}")
my_fun(100)
print(f"After, my_var={my_var}")
