#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def parent():
    """TODO: Function docstring."""
    print('Printing from the parent() function.')

    def first_child():
        """TODO: Function docstring."""
        print('Printing from the first_child() function.')

    def second_child():
        """TODO: Function docstring."""
        print('Printing from the second_child() function.')

    second_child()
    first_child()


def main():
    """Starting point of the program."""
    parent()


if __name__ == '__main__':
    main()
