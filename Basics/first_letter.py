#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def main():
    """Starting point of the program."""
    response = input('Tell me your password: ')
    first_letter = response[0].upper()
    print(f'The first letter you entered was: {first_letter!r}')


if __name__ == '__main__':
    main()

