#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import pandas


def display_csv(csv_file):
    """TODO: Function docstring."""
    data_frame = pandas.read_csv(csv_file, index_col='Name',
                                 parse_dates=['Hire Date'])
    print(data_frame)


def main():
    """Starting point of the program."""
    csv_file = 'hrdata.csv'
    display_csv(csv_file)


if __name__ == '__main__':
    main()
