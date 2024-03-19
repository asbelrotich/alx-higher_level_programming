#!/usr/bin/python3
import sys


def print_arguments():
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")
    else:
        print("{} arguments:" .format(num_args))
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()
