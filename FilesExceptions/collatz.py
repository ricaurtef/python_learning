#!/usr/bin/env python3
"""
Practice Project: Write a function named collatz() that has one paremeter named
number. If number is even, the collatz() should print number // 2 and return
this value. If number is odd, the colltz() sould print and return 3 * number +
1.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import sys


def collatz(number):
    """The collatz sequence."""
    if not number % 2:
        return number // 2
    return (3*number) + 1


def main():
    """Entry point."""
    for _ in range(3):
        try:
            number = int(input('Enter a number > '))
        except ValueError:
            print('You must enter an integer.')
            continue
        else:
            while number != 1:
                number = collatz(number)
                print(number, end=' ')
            print()
        break
    else:
        print('Is it that hard to enter an integer?\nProgram terminated.')
        sys.exit(1)


if __name__ == '__main__':
    main()
