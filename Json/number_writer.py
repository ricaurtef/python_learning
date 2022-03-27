#!/usr/bin/env python3
"""number_writer.py: playing with the json module."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import json
from pathlib import Path
from random import randint


def main():
    """Starting point of the program."""
    filename = Path() / 'numbers.json'

    try:
        with filename.open(mode='r') as fobj:
            numbers = json.load(fobj)
    except FileNotFoundError:
        numbers = [randint(1, 20) for _ in range(6)]
        with filename.open(mode='w') as fobj:
            json.dump(numbers, fobj)
        print(f'The "{filename.name}" file was created successfully.')
    else:
        print(numbers)


if __name__ == '__main__':
    main()
