def greeting():
    print("Hello Student")

def launch_missile(count):
    print(f"{count} misslies launched.")

def square(n):
    sq = n**2
    return sq

def sq_cube(n):
    sq = n**2
    cb = n**3
    return sq, cb

def print_vector(h, x, y, z=10):
    print(f"Vector is: h={h}, x={x}, y={y}, z={z}")



def my_sum(a,b,*args,**kwargs):
    print(f"a = {a}, {type(a)}")
    print(f"b = {b}, {type(b)}")
    print(f"args = {args}, {type(args)}")
    print(f"kwargs = {kwargs}, {type(kwargs)}")

if __name__ == '__main__':
    launch_misslie(10)
    result = square(5)
    print(result)
    greeting()