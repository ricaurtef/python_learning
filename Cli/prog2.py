#!/usr/bin/env python3
"""Argparse examples: Getting a little more advanced."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


from argparse import ArgumentParser


def args():
    """Handle command-line arguments and options."""
    parser = ArgumentParser(
        prog='prog',
        description='calculate X to the power of Y',
    )

    # Example 01: uses verbosity level to display more text instead.
    # parser.add_argument('x', type=int, help='the base')
    # parser.add_argument('y', type=int, help='the exponent')
    # parser.add_argument('-v', '--verbosity', action='count', default=0,
    #                     help='increase the output verbosity')

    # Example 02: conflicting options.
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('x', type=int, help='the base')
    parser.add_argument('y', type=int, help='the exponent')

    return parser.parse_args()


def main():
    """Entry point."""
    argv = args()
    answer = pow(argv.x, argv.y)

    # Example 01.
    # if argv.verbosity >= 2:
    #     print(f'Running {__file__!r}')
    # elif argv.verbosity >= 1:
    #     print(f'{argv.x}^{argv.y} == ', end='')
    # print(answer)

    # Example 02.
    if argv.quiet:
        print(answer)
    elif argv.verbose:
        print(f'{argv.x} to the power {argv.y} equals {answer}')
    else:
        print(f'{argv.x}^{argv.y} == {answer}')


if __name__ == '__main__':
    main()
