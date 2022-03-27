#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from decorators import timer


@timer
def waste_some_time(num_times):
    """TODO: Function docstring."""
    for _ in range(num_times):
        sum([pow(i, 2) for i in range(10_000)])


def main():
    """Starting point of the program."""
    waste_some_time(999)


if __name__ == '__main__':
    main()
