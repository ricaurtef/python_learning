#!/usr/bin/env python3
"""Dictionary data structure exercise."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def total_brought(guests: dict, item: str) -> int:
    """Return the total of a given item."""
    return sum(count.get(item, 0) for count in guests.values())


def main():
    """Entry point."""
    all_guests = {
        'alice': {'apples': 5, 'pretzels': 12},
        'bob': {'ham_sandwiches': 3, 'apples': 2},
        'carol': {'cups': 3, 'apple_pies': 1},
    }
    items = ('apples', 'cups', 'cakes', 'ham_sandwiches', 'apple_pies')

    print('Number of things being brought:')
    for item in items:
        print(f'- {item.title()} -> {total_brought(all_guests, item)}')


if __name__ == '__main__':
    main()
