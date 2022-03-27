#!/usr/bin/env python3
"""Table Printer

Write a function named print_table() that takes a list of lists of
strings and displays it in a well-organized table with each column
right-justified.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from tabulate import tabulate


class Table:
    """A simple class to handle tabular data."""

    def __init__(self, table):
        """Initialize the table class."""
        self.table = table

    def __repr__(self):
        """Transponse and pretty print the table right-justified."""
        transponsed_table = list(zip(*self.table))

        return tabulate(transponsed_table, tablefmt='psql', stralign='right')


def main():
    """Entry point."""
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose'],
    ]

    table = Table(table_data)
    print(table)


if __name__ == '__main__':
    main()
