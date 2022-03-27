#!/usr/bin/env python3
"""Exception Handling."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def spam(divider):
    """Simple division."""
    return 42 / divider


def main():
    """Entry point."""
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(1))
    except ZeroDivisionError:
        print('Error: Invalid argument.')


if __name__ == '__main__':
    main()
