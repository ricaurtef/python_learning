#!/usr/bin/env python3
"""Table Printer:

Write a function named print_table() that takes a list of lists of
strings and displays it in a well-organized table with each column
right-justified. Assume that all the inner lists will contain the same
number of strings.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def print_table(data):
    """Transponse and pretty print the table right-justified."""
    for i in range(len(max(data))):
        for row in data:
            width = max(len(x) for x in row)
            print(f'{row[i]:>{width}}', end=' ')
        print()


def main():
    """Entry point."""
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose'],
    ]

    print_table(table_data)


if __name__ == '__main__':
    main()
