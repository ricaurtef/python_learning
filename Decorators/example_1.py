#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def say_hello(name):
    """TODO: Function docstring."""

    return f'Hello, {name}!'


def be_awesome(name):
    """TODO: Function docstring."""

    return f'Yo {name}, together we are the awesomest!'


def greet_bob(greeter_func):
    """TODO: Function docstring."""

    return greeter_func('Bob')


def main():
    """Starting point of the program."""
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))


if __name__ == '__main__':
    main()
