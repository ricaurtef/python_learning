#! /usr/bin/env python3
"""Challenge: Wax Poetic.

Using randomly selected words, generate and display a poem with the
structure inspired by Clifford Pickover.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'

from random import choice


# Global definitions.
nouns = [
    'fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango',
     'extrovert', 'gorilla',
]
verbs = [
    'kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes',
    'curdles',
]
adjectives = [
    'furry', 'balding', 'incredulous', 'fragrant', 'exuberant',
    'glistening',
]
prepositions = [
    'against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like',
    'over', 'within',
]
adverbs = [
    'curiously', 'extravagantly', 'tantalizingly', 'furiously',
    'sensuously',
]


def words(list_words: list, num_words: int) -> list:
    """Return randomly selected unique 'num_words' number of words."""
    random_words = []

    while True:
        word = choice(list_words)
        if len(random_words) == num_words:
            break
        elif word not in random_words:
            random_words.append(word)

    return random_words


def article(adjective: str) -> str:
    """Return the right indefinite article for a given adjective."""

    return 'an' if adjective.startswith(tuple('aeiou')) else 'a'


def main():
    """Starting point of the program."""
    # Select the lists of words that will make up the poem.
    noun1, noun2, noun3 = words(nouns, 3)
    verb1, verb2, verb3 = words(verbs, 3)
    adj1, adj2, adj3 = words(adjectives, 3)
    prep1, prep2 = words(prepositions, 2)
    adverb = words(adverbs, 1)[0]
    art1 = article(adj1)
    art2 = article(adj3)

    # Display the poem.
    print(
        f'{art1.title()} {adj1} {noun1}\n\n'
        f'{art1.title()} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n'
        f'{adverb}, the {noun1} {verb2}\n'
        f'the {noun2} {verb3} {prep2} {art2} {adj3} {noun3}.'
    )


if __name__ == '__main__':
    main()
