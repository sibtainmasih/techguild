num = input("Enter a number: ")

# Check if the entered value is digit

# if not num.isdigit():
#    print("Entered value is not digit")
#    exit(1)

num = int(num)

if num>0:
    print(f"Number {num} is positive")
elif num<0:
    print("Number {num} is negative")
else:
    print("Number is zero")


