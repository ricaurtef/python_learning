#!/usr/bin/env python3
"""Argparse example."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import sys
from argparse import ArgumentParser
from pathlib import Path


def args():
    """Handle command-line arguments and options."""
    # Create the parser.
    parser = ArgumentParser(
        prog='myls',
        description='List the content of a directory.',
    )

    # Add the arguments.
    parser.add_argument('dirname', help='the directory to list')

    # Execute the parse_args() method.
    return parser.parse_args()


def main():
    """Entry point."""
    argv = args()
    directory = Path() / argv.dirname

    try:
        if not directory.is_dir():
            raise NotADirectoryError
    except NotADirectoryError:
        print(f'Not found: the directory does not exist: {directory}')
        sys.exit(1)
    else:
        for file_ in directory.iterdir():
            print(file_.name)


if __name__ == '__main__':
    main()
