#! /usr/bin/env python3
"""TODO: Module docstring."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from my_package import module1, module2
from my_package.my_subpackage import module3


def main():
    """Starting point of the program."""
    module1.greet('pythonista')
    module2.depart('pythonista')

    for person in module3.people:
        module1.greet(person)


if __name__ == '__main__':
    main()
