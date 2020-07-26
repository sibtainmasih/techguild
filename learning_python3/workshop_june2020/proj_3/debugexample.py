def multiply(x, y):
    result = x*y 
    return result


if __name__ == "__main__":
    print("Line 1")
    print("Line 2")
    x = '10'
    y = 3
    #print(f"x={x}")
    print(f"{x=}")
    print(f"{y=}")
    answer = multiply(x,y)
    print("Line after function call")
    print(f"{answer=}")
    print("Program terminates.")