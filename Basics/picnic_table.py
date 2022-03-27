#!/usr/bin/env python3
"""Manipulating strings."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def print_picnic(items, lwidth, rwidth):
    """Tabulate picnic items."""
    print('picnic items'.upper().center(lwidth + rwidth, '-'))
    # print(f'{"picnic items".upper():-^{lwidth + rwidth}}')
    for item, count in items.items():
        print(f'{item:.<{lwidth}}{count:{rwidth}}')


def main():
    """Entry point."""
    picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

    for lwidth, rwidth in [(12, 5), (20, 6)]:
        print_picnic(picnic_items, lwidth, rwidth)
        print()


if __name__ == '__main__':
    main()
