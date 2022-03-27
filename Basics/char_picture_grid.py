#!/usr/bin/env python3
"""Another list exercise."""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import time


def main():
    """Entry point."""
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
    ]

    # Traversing the grid.
    # First way: using for loops.
    for xaxis in range(len(max(grid))):
        for yaxis, _ in enumerate(grid):  # Suggested by pylint.
            print(grid[yaxis][xaxis], end='')
        print()

    # Second way: using the zip function.
    for row in zip(*grid):
        print(''.join(row))
        time.sleep(0.5)


if __name__ == '__main__':
   main()
