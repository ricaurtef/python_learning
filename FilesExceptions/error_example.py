#!/usr/bin/env python3
"""Gettiing the Traceback as a String."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import traceback


def spam():
    """Spam."""
    bacon()


def bacon():
    """Bacon."""
    raise Exception('This is the error message.')


def main():
    """Entry point."""
    try:
        spam()
    except Exception:
        error_file = 'error_info.log'
        with open(error_file, 'w') as fobj:
            fobj.write(traceback.format_exc())
            print(f'The traceback info was written to: {error_file}.')


if __name__ == '__main__':
    main()
