#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def my_decorator(func):
    """TODO: Function docstring."""
    def wrapper():
        print('Something is happening before the function is called.')
        func()
        print('Something is happening after the function is called.')

    return wrapper


def say_whee():
    """TODO: Function docstring."""
    print('Whee!')


def main():
    """Starting point of the program."""
    say_something = my_decorator(say_whee)
    say_something()


if __name__ == '__main__':
    main()
