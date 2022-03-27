#!/usr/bin/env python3
"""A simple example of recursion."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def iterative_test(low, high):
    """Print out numbers between low and high using iteration."""
    while low <= high:
        print(low, end=' ')
        low += 1
    print()


def recursive_test(low, high):
    """Print out numbers between low and high using recursion."""
    if low <= high:
        print(low, end=' ')
        recursive_test(low+1, high)


def main():
    """Starting point of the program."""
    # Iterative test.
    iterative_test(2, 10)

    # Recursive test.
    recursive_test(2, 10)
    print()


if __name__ == '__main__':
    main()
