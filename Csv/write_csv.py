#!/usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import csv
from pathlib import Path


def write_employees(csv_file, employees, fieldnames=None):
    """TODO: Function docstring."""
    fieldnames = ('name', 'dept', 'birth_month')

    with open(csv_file, mode='w', encoding='utf-8') as fobj:
        employees_writer = csv.writer(fobj, delimiter=',', quotechar="'",
                                      quoting=csv.QUOTE_MINIMAL)
        employees_writer.writerow(fieldnames)
        employees_writer.writerows(employees)

        # Another way of writing.
        # for employee in employees:
        #     employees_writer.writerow(employee)


def main():
    """Starting point of the program."""
    filename = Path() / 'employee_file.csv'
    employees = [
        ('Smith, John', 'Accounting', 'November'),
        ('Meyers, Erica', 'IT', 'March'),
    ]

    # Save employees info to a csv file.
    try:
        if not filename.exists():
            raise FileNotFoundError
    except FileNotFoundError:
        write_employees(filename, employees)
        print(f'The "{filename}" file was created successfully.')
    else:
        print(f'The "{filename}" file already exists.')


if __name__ == '__main__':
    main()
