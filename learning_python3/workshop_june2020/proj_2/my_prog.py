def sum_all(a,b, *args):
    result = a+b
    for n in args:
        result +=n
    return result

print(__name__)

if __name__ == '__main__':
    r = sum_all(10,30,40)
    print(f"Result = {r}")