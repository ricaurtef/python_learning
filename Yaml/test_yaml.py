#! /usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'

from yaml import load_all, Loader
from pprint import pprint


def main():
    """Starting point of the program."""
    filename = 'test_yaml.yml'

    with open(filename, mode='r') as fobj:
        documents = list(load_all(fobj, Loader=Loader))

    # Display the content of the yaml file.
    pprint(documents)


if __name__ == '__main__':
    main()
