#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)

    return head


def main():
    """Starting point of the program."""
    filename = __file__
    breakpoint()  # Calling the debugger.
    filename_path = get_path(filename)
    print(f'path = {filename_path}')


if __name__ == '__main__':
    main()
