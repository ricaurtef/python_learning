#!/usr/bin/env python3
"""Debugging: Raise an exception."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def box_print(symbol, width, height):
    """TODO: Write docstring."""
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')

    if width <= 2 or height <= 2:
        raise Exception('Width/Height must be greater than 2.')

    print(symbol * width)
    for _ in range(height - 2):
        print(f"{symbol}{' ' * (width - 2)}{symbol}")
    print(symbol * width)


def main():
    """Entry point."""
    sym_list = (
        ('*', 4, 4),
        ('O', 20, 5),
        ('x', 1, 3),
        ('ZZ', 3, 3),
    )

    for sym, width, height in sym_list:
        try:
            box_print(sym, width, height)
        except Exception as error:  # An example of what NOT to do.
            print(f'An exception happend: {error}')


if __name__ == '__main__':
    main()
