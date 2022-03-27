#!/usr/bin/env python3
"""Project: Phone Number and Email Address Extractor.

Finds phone numbers and email addresses on the clipboard.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import re
import sys

import pyperclip


def get_phone_number(phone):
    """
    Checks whether a string matches the american phone number pattern.

    """
    phone_regex = re.compile(r'''
        (?P<code>\d{3}|\(\d{3}\))?              # Area code.
        (?:[-\s.])?                             # Separator.
        (?P<first>\d{3})                        # First 3 digits.
        (?:[-\s.])                              # Separator.
        (?P<last>\d{4})                         # Last 4 digits.
        (\s*(ext|x|ext.)\s*(?P<ext>\d{2,5}))?   # Extension.
    ''', re.VERBOSE)

    return phone_regex.finditer(phone)


def get_email(email):
    """Checks whether a string matches an email pattern."""
    email_regex = re.compile(r'''(
       [-\w._%+]+           # Username.
       @                    # @ symbol.
       [-\w.]+              # Domain name.
       (\.[a-zA-Z]{2,4})    # Dot-something.
    )''', re.VERBOSE)

    return email_regex.finditer(email)


def main():
    """Entry point."""
    text = pyperclip.paste()
    matches = []

    for phone in get_phone_number(text):
        phone_number = (f'{phone.group("code")}-{phone.group("first")}'
                        f'-{phone.group("last")}')
        if phone.group('ext'):
            phone_number += ' x' + phone.group('ext')
        matches.append(phone_number)

    for email in get_email(text):
        matches.append(email.group())

    if not matches:
        print('No phones numbers or email addresses found.')
        sys.exit()

    # Copy results to the clipboard.
    pyperclip.copy('\n'.join(matches))

    # Some human-friendly output.
    print('Copied to the clipboard:')
    print('\n'.join(matches))


if __name__ == '__main__':
    main()
