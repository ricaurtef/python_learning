#!/usr/bin/env python3
"""Lists practice project."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def comma_code(value):
    """
    Returns a string with all the list item separated by a comma and a space,
    with _and_ inserted before the last item.
    """
    last_item = value[-1]
    return ', '.join(value[:-1]) + f' and {last_item}.'


def main():
    """Entry point."""
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))


if __name__ == '__main__':
    main()
