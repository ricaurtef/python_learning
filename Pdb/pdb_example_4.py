#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import util


def main():
    """Starting point of the program."""
    filename = __file__
    breakpoint()  # Calling the debugger.
    filename_path = util.get_path(filename)
    print(f'path = {filename_path}')


if __name__ == '__main__':
    main()
