#! /usr/bin/env python3
"""Challenge: Cats With Hats.

You have one hundred cats.

One day, you decide to arrange all your cats in a giant circle.
Initailly, none of your cats has a hat on. You walk around the circle a
hundred times, always starting with the first cat. Each time you stop
at a cat, you check if it has a hat on. If it doesn't, then you put a
hat on it. If it does, then you take the hat off.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


def cats_hats(num_cats: int = 100) -> dict:
    """TODO: function docstring."""
    cats = {i: False for i in range(1, num_cats+1)}

    for round_ in range(1, num_cats+1):
        for cat in range(1, num_cats+1):
            if cat % round_ == 0:
                if not cats[cat]:
                    cats[cat] = True
                else:
                    cats[cat] = False

    return cats


def main():
    """Starting point of the program."""
    cats_with_hats = [str(k) for k, v in cats_hats().items() if v]

    # Display every cat with a hat.
    print(f"Cats with hats: {', '.join(cats_with_hats)}.")


if __name__ == '__main__':
    main()
