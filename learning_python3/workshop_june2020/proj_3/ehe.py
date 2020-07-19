import sys

def log(msg):
    print(f"[DEBUG]  {msg}")


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        log(f"{e!r}")
        raise
    
def main(argv):
    try:
        num1 = int(argv[1])
        num2 = int(argv[2])
        result = divide(num1, num2)
        print(result)
    except ValueError:
        print("The value is of incorrect type. Provide integers only")
        return
    except Exception as e:
        print(f"Wide net to catch all the exceptions except ValueError. {e!r}")    
    else:
        print("Else - Executes only when there is no exception raised in try block.")
    finally:
        print("Finally - Execute in any scenario.")    

    print("Program terminated gracefully.")

if __name__ == "__main__":
    main(sys.argv)