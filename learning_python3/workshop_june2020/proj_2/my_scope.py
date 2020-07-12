
my_var=20

def modify_var(x):
    global my_var
    my_var = x
    print(f"Inside function, my_var = {my_var}")

print(f"Before: my_var={my_var}")
modify_var(100)
print(f"After: my_var={my_var}")