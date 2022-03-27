#!/usr/bin/env python3
"""Pattern Matching With Regular Expressions.

Example: find an american phone number in a stirng without regular
expressions.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def is_phone_number(text) -> bool:
    """
    Check whether a string matches the american phone number pattern:
    three numbers, a hyphen, three numbers, a hyphen, and four numbers.

    Example:

        >>> is_phone_number(415-555-4242)
        True
    """
    if len(text) == 12 and text.count('-') == 2:
        if text[3] == text[7] == '-':
            return all(num.isdecimal() for num in text.split('-'))

    return False


def main():
    """Starting point of the program."""
    # values = ('415-555-4242', 'Moshi moshi', 'abc-def-4242')

    # for value in values:
    #     print(f'Is {value} a phone number?\n{is_phone_number(value)}')

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print(f'Phone number found: {chunk}.')

    print('Done.')


if __name__ == '__main__':
    main()
