#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def cube(number: float, /):
    """Return a number raised to the third power."""
    return pow(number, 3)


def main():
    """Starting point of the program."""
    number = float(input('Enter a number: '))
    print(f'{number} raised to the third power is: {cube(number)}')


if __name__ == '__main__':
    main()

