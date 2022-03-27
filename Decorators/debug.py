#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from decorators import debug


@debug
def make_greeting(name, age=None):
    """TODO: Function docstring."""
    if age is None:
        return f'Howdy {name}!'
    return f'Whoa {name}! {age} already, you are growing up!'


def main():
    """Starting point of the program."""
    name = 'ruben'
    age = 39
    print(make_greeting(name, age))


if __name__ == '__main__':
    main()
