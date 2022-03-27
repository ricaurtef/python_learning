#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def parent(num):
    """TODO: Function docstring."""
    def first_child():
        """TODO: Function docstring."""

        return 'Hi, I am Emma.'

    def second_child():
        """TODO: Function docstring."""

        return 'Call me Liam.'

    if num == 1:
        return first_child
    return second_child


def main():
    """Starting point of the program."""
    first = parent(1)
    second = parent(2)

    # Just references to the inner functions.
    print(first)
    print(second)

    # Now we can use _first_ and _second_ as if they are regular functions.
    print(first())
    print(second())


if __name__ == '__main__':
    main()
