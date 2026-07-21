import sys
from modes.ascii import ascii
from modes.color import color

def main():
    if len(sys.argv) < 2:
        print("usage: python main.py <mode>")
        print("available modes: ascii, color")
        sys.exit(1)
    elif sys.argv[1] == "ascii":
        ascii()
    elif sys.argv[1] == "color":
        color()
    else:
        print("invalid mode")
        print("valid modes: ascii, color")
        sys.exit(1)

if __name__ == '__main__':
    main()