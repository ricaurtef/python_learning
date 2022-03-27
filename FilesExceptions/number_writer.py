#!/usr/bin/env python3
"""Using json.dump()"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json
from pathlib import Path


def main():
    """Entry point."""
    numbers = [2, 3, 5, 7, 11, 13]
    filename = Path('numbers.json')

    with open(filename, mode='w') as file_object:
        json.dump(numbers, file_object)


if __name__ == '__main__':
    main()
