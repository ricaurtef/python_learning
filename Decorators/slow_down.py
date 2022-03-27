#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from decorators import slow_down


@slow_down
def countdown(from_number):
    """TODO: Function docstring."""
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1)


def main():
    """Starting point of the program."""
    countdown(3)


if __name__ == '__main__':
    main()
