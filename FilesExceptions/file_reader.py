#! /usr/bin/env python3
"""Files and exceptions:

Reading an Entire File.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import re
import sys
from pathlib import Path


def main():
    """Entry point."""
    # Example 01: Without the Path class.
    # with open('pi_digits.txt') as file_object:
    #     contents = file_object.read()

    # print(contents.rstrip())

    # Example 02: With the Path class.
    # filename = Path('pi_digits.txt')
    # print(filename.read_text().rstrip())

    # Example 03: Reading line by line without the Path class.
    # filename = 'pi_digits.txt'

    # with open(filename) as file_object:
    #     for line in file_object:
    #         print(line)

    # Example 04: Reading line by line with the Path class.
    # filename = Path('pi_digits.txt')

    # with open(filename) as file_object:
    #     for line in file_object:
    #         print(line.rstrip())

    # Example 05: Making a list of lines from a file.
    filename = Path('pi_million_digits.txt')

    with open(filename, encoding='utf-8') as file_object:
        lines = file_object.readlines()

    # Now playing with the list.
    pi_string = ''.join([line.strip() for line in lines])

    print(f'Pi\t{pi_string[:52]}...\n'
          f'Length\t{len(pi_string)}')

    # Example 06: Is your b-day contained in Pi?
    bday_regex = re.compile(r'''(
        (?:0[1-9]|1[0-2])           # Month
        (?:0[1-9]|[12]\d|3[01])     # Day
        (?:\d{2})                   # Year
    )''', re.VERBOSE)
    birthday = input('Enter your birthday (mmddyy): ')
    date = bday_regex.match(birthday)

    if date is not None:
        if date.group() in pi_string:
            msg = 'Cool! Your b-day appears'
        else:
            msg = 'Your b-day does not appear'
        print(msg, 'in the first million digits of Pi.')
    else:
        print('You introduced an invalid date.')
        sys.exit(1)


if __name__ == '__main__':
    main()
