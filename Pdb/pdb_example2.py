#!/usr/bin/env python3
"""Getting started: Printing Expressions."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from pathlib import Path


def get_path(filename):
    """Return file's path or empty string fi no path."""
    dirname = Path(filename).absolute().parent
    breakpoint()  # Same as: import pdb; pdb.set_trace()

    return dirname


def main():
    """Entry point."""
    filename = __file__
    print(f'path = {get_path(filename)}')


if __name__ == '__main__':
    main()
