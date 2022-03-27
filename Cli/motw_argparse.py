#!/usr/bin/env python3
"""TODO: Module Description."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from argparse import ArgumentParser


def args():
    """Handle command-line arguments and options."""
    parser = ArgumentParser(
        prog='tester',
        description='This is a PyMOTW sample program',
    )
    parser.add_argument('-v', action='version', version='%(prog)s 0.1')

    return parser.parse_args()


def main():
    """Entry point."""
    argv = args()


if __name__ == '__main__':
    main()
