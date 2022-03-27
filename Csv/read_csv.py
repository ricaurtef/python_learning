#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import csv


def display_csv(csv_file, tabs=4):
    """TODO: Function docstring."""
    with open(csv_file, mode='r', encoding='utf-8') as fobj:
        csv_reader = csv.reader(fobj, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index == 0:
                print(f'Colums names are: {", ".join(row)}.')
                continue
            print(f'{" " * tabs}{index}) {row[0]} works in the {row[1]} '
                  f'department, and was born in {row[2]}.')
        print(f'Processed {index + 1} lines.')


def main():
    """Starting point of the program."""
    filename = 'employee_bday.csv'
    display_csv(filename)


if __name__ == '__main__':
    main()
