#!/usr/bin/env python3
"""Practice project."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def display_inventory(inventory):
    """Display the player's inventory."""
    total_items = 0
    print('Inventory')
    for item, total in inventory.items():
        print(f'{total:02d}  {item.capitalize()}')
        total_items += total
    print(f'Total number of items: {total_items}')


def add_inventory(inventory, items) -> dict:
    """Update player's inventory."""
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def main():
    """Entry point."""
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_inventory(stuff, dragon_loot)
    display_inventory(inv)


if __name__ == '__main__':
    main()
