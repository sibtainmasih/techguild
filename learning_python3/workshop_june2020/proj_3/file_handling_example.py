import sys
import os

file_path= os.path.join('.', 'data', 'xyz32.txt')

# os.path.exists(file_path)

# content = sys.argv[1]

# with open(file_path, mode="a+", encoding="utf-8") as fp:
#     fp.write( f"{content}\n")
#     fp.seek(0)
#     print(fp.readlines())


# Look Before You Leap (LBYL)

# if os.path.exists(file_path):
#     with open(file_path, mode="r", encoding="utf-8") as fp:
#         print(fp.readlines())
# else:
#     print(f"{file_path} does not exist.")

# Easier to ask forgiveness than permission (EAFP)

with open(file_path, mode="r", encoding="utf-8") as fp:
    print(fp.readlines())










