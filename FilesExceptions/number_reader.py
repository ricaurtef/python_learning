#!/usr/bin/env python3
"""Using json.load()"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json
from pathlib import Path


def main():
    """Entry point."""
    filename = Path('numbers.json')

    with open(filename) as file_object:
        numbers = json.load(file_object)

    print(numbers)


if __name__ == '__main__':
    main()
