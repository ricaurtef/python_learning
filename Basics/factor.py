#! /usr/bin/env python3
"""Challenge: Find the Factors of a Number.

A factor of a positive integer _n_ is any positive integer less than or equal
to _n_ that divides _n_ with no remainder.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Starting point of the program."""
    number = int(input('Enter a positive integer: '))
    pad = len(str(number))

    for divisor in range(1, number+1):
        if number % divisor == 0:
            print(f'{divisor:0{pad}d} is a factor of {number}')


if __name__ == '__main__':
    main()
