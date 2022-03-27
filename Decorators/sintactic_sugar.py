#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from datetime import datetime


def not_during_night(func):
    """TODO: Function docstring."""
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

    return wrapper


@not_during_night
def say_whee():
    """TODO: Function docstring."""
    print('Whee!')


def main():
    """Starting point of the program."""
    say_whee()


if __name__ == '__main__':
    main()
