#!/usr/bin/env python3
"""Simple flow control exercise."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from random import randint


def main():
    """Entry point."""
    spam = randint(1, 3)
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')


if __name__ == '__main__':
    main()
