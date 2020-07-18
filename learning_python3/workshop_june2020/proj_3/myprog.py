import sys

def banner(msg, symbol="#"):
    line = len(msg) * symbol
    print(line)
    print(msg)
    print(line)

def main():
    print("Hello World")

print(__name__)

if __name__ == "__main__":
    main()
    banner("Tech Guild", symbol='*')
    print(sys.argv)
