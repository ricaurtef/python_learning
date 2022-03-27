#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def to_leetspeak(string):
    """TODO: Function Docstring."""
    patterns = [
        ('a', '4'),
        ('b', '8'),
        ('e', '3'),
        ('l', '1'),
        ('o', '0'),
        ('s', '5'),
        ('t', '7'),
    ]

    for pattern in patterns:
        string = string.replace(*pattern)

    return string


def main():
    """Starting point of the program."""
    response = input('Enter some text: ')
    print(to_leetspeak(response))


if __name__ == '__main__':
    main()
