#!/usr/bin/env python3
"""Debugging: pdb module."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    breakpoint()
    head, tail = os.path.split(filename)

    for char in tail:
        pass  # Check filename char.

    return head


def main():
    """Entry point."""
    filename = __file__
    filename_path = get_path(filename)
    print(f'path = {filename_path}.')


if __name__ == '__main__':
    main()
