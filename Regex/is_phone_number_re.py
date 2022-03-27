#!/usr/bin/env python3
"""Pattern Matching With Regular Expressions.

Example: find an american phone number in a string with regular
expressions.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import re


def is_phone_number(text) -> bool:
    """
    Check whether a string matches the american phone number pattern:
    three numbers, a separator, three numbers, a separator, and four
    numbers.

    Example:

        >>> is_phone_number(415-555-4242)
        True
    """
    phone_regex = re.compile(r'''(
        (?:\d{3}|\(\d{3}\))             # Area code.
        (?:[-\s.])                      # Separator.
        (?:\d{3})                       # First 3 digits.
        (?:[-\s.])                      # Separator.
        (?:\d{4})                       # Last 4 digits.
        (?:\s*(ext|ext.)\s*\d{2,5})?    # Extension.
    )''', re.VERBOSE)

    return phone_regex.match(text)


def main():
    """Starting point of the program."""
    # values = ('415-555-4242', 'Moshi moshi', 'abc-def-4242')

    # for value in values:
    #     print(f'Is {value} a phone number?\n{is_phone_number(value)}')

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

    # Original example.
    # for i in range(len(message)):
    #     chunk = message[i:i+12]
    #     if is_phone_number(chunk) is not None:
    #         print(f'Phone number found: {chunk}.')

    # With an assignment expression.
    for i in range(len(message)):
        if phone := is_phone_number(message[i:i+12]):  # Walrus operator.
            print(f'Phone number found: {phone.group()}.')

    print('Done.')


if __name__ == '__main__':
    main()
