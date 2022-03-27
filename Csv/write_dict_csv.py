#!/usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import csv
from pathlib import Path


def write_employees(csv_file, employees):
    """TODO: Function docstring."""
    with open(csv_file, mode='w', encoding='utf-8') as fobj:
        fieldnames = ('name', 'department', 'birth_month')
        employees_writer = csv.DictWriter(fobj, fieldnames=fieldnames,
                                          quotechar="'",
                                          quoting=csv.QUOTE_MINIMAL)
        employees_writer.writeheader()
        employees_writer.writerows(employees)

        # Anothe way of writing.
        # for employee in employees:
        #     file_writer.writerow(employee)


def main():
    """Starting point of the program."""
    filename = Path() / 'employee_dict_file.csv'
    employees = [
        {
            'name': 'Smith, John',
            'department': 'Accounting',
            'birth_month': 'November',
        },
        {
            'name': 'Meyers, Erica',
            'department': 'Accounting',
            'birth_month': 'March',
        },
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
