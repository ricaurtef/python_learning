#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import csv


def display_csv(csv_file, tabs=4):
    """TODO: Function docstring."""
    with open(csv_file, mode='r', encoding='utf-8') as fobj:
        csv_reader = csv.DictReader(fobj, delimiter=',')
        for index, row in enumerate(csv_reader, start=1):
            if index == 1:
                print(f'Colums names are: {", ".join(row)}.')
            print(f'{" " * tabs}{index}) {row["name"]} works in the '
                  f'{row["department"]} department, and was born in '
                  f'{row["birthday month"]}.')
        print(f'Processed {index + 1} lines.')


def main():
    """Starting point of the program."""
    filename = 'employee_bday.csv'
    display_csv(filename)


if __name__ == '__main__':
    main()
