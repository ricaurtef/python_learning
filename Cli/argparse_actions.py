#!/usr/bin/env python3
"""
Example program showing each action type, with the miniumm conifguration
needed for each to work.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from argparse import ArgumentParser


def args():
    """Handle command-line positional arguments and options."""
    parser = ArgumentParser(prog='argparse_actions')
    # Default action: store.
    parser.add_argument('-s', dest='simple_value',
                        help='store a simple value')

    # Action: store_const.
    parser.add_argument(
        '-c', action='store_const',
        dest='constant_value',
        const='value to store',
        help='store a constant value',
    )

    # Action: store_true (default: False)
    parser.add_argument(
        '-t', action='store_true',
        dest='bool_true',
        help='set a switch to true',
    )

    # Action: store_false (default: True)
    parser.add_argument(
        '-f', action='store_false',
        dest='bool_false',
        help='set a switch to false',
    )

    # Action: append (default: [])
    parser.add_argument(
        '-a', action='append',
        dest='collection',
        help='add repeated values to a list',
    )

    # Action: append_const (default: [])
    parser.add_argument(
        '-A', action='append_const',
        dest='constant_collection',
        const='first value to append',
        help='add same value to a list',
    )

    # Action: append_const (default: [])
    parser.add_argument(
        '-B', action='append_const',
        dest='constant_collection',
        const='second value to append',
        help='add same value to a list',
    )

    # Action: version.
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')

    return parser.parse_args()


def main():
    """Entry point."""
    argv = args()
    print(f'simple value        = {argv.simple_value}')
    print(f'constant value      = {argv.constant_value}')
    print(f'bool_true           = {argv.bool_true}')
    print(f'bool_false          = {argv.bool_false}')
    print(f'collection          = {argv.collection}')
    print(f'constant collection = {argv.constant_collection}')


if __name__ == '__main__':
    main()
