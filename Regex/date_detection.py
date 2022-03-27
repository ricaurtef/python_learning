#!/usr/bin/env python3
"""Regex exercises: Date Detection.

Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and
the years range from 1000 to 2999. Note that if the day or month is a single
digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or
for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April,
June, September, and November have 30 days, February has 28 days, and the rest
of the months have 31 days. February has 29 days in leap years. Leap years are
every year evenly divisible by 4, except for years evenly divisible by 100,
unless the year is also evenly divisible by 400.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import re


def is_valid_date(date):
    """Checks the validity of a given date.

    Date format: DD/MM/YYYY or DD-MM-YYY.
    """
    date_regex = re.compile(r'''
        (?P<day>0[1-9]|[12][0-9]|3[01])     # Days between 01 and 31.
        (?P<sep>[/-])                       # Date separator.
        (?P<month>0[1-9]|1[0-2])            # Month.
        (?P=sep)                            # Date separator.
        (?P<year>[12][0-9]{3})              # Years between 1000 and 2999.
    ''', re.VERBOSE)
    match_object = date_regex.match(date)

    if match_object is not None:
        day = int(match_object.group('day'))
        month = int(match_object.group('month'))
        year = int(match_object.group('year'))

        if (month in (4, 6, 9, 11)) and (day > 30):
            return False
        if (year % 4) == 0:
            if (year % 100 == 0) and (year % 400 == 0):
                if (month == 2) and (day > 29):
                    return False
        elif month == 2 and day > 28:
            return False
    else:
        return False

    return True


def main():
    """Starting point of the program."""
    date = '29-02-2012'

    if is_valid_date(date):
        print(f'{date!r} is a valid date.')
    else:
        print(f'{date!r} is not a valid date.')


if __name__ == '__main__':
    main()
