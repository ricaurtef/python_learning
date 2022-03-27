#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import sys


def main():
    """Starting point of the program."""
    for _ in range(3):
        base = input('Enter a base: ')
        exponent = input('Enter an exponent: ')
        if not base or not exponent:
            print('You must enter both the base and the exponent.')
            continue
        result = pow(float(base), float(exponent))
        print(f'{base} to the power of {exponent} = {result}')
        break
    else:
        print('You reached the maximum number of attempts. Program terminated.')
        sys.exit(1)


if __name__ == '__main__':
    main()
