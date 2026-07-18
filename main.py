import sys
from modes.ascii import ascii
from modes.color import color

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode>")
        sys.exit(1)
    elif sys.argv[1] == "ascii":
        ascii()
    elif sys.argv[1] == "color":
        color()
    else:
        print("invalid mode.\navailable modes: ascii, color")

if __name__ == '__main__':
    main()