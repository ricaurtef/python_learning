#!/usr/bin/env python3
"""
Strings:

Pig Latin is a silly made-up language that alters English words. If a
word begins with a vowel, the word yay is added to the end of it. If a
word begins with a consonant or consonant cluster (like ch or gr), that
consonant or cluster is moved to the end of the word followed by ay.
"""

__author__ = 'Ruben Ricaurte <ricaurtef@gmail.com>'


import re


def start_with_consonant(word):
    """
    Alter words that start with a consonant or consonant cluster
    (like ch or gr).
    """
    # Case insensitive match
    consonants = re.compile(r'([^aeiou]+)([aeiouy]\w*)', re.I)
    mo_consonants = consonants.match(word)
    suffix = 'AY' if word.isupper() else 'ay'
    altered_word = f'{mo_consonants.group(2)}{mo_consonants.group(1)}{suffix}'

    return altered_word


def start_with_vowel(word):
    """Alter words that start with a vowel."""
    # Case insensitive match
    vowels = re.compile(r'([aeiou]\w*)', re.I)
    mo_vowels = vowels.match(word)
    suffix = 'YAY' if word.isupper() else 'yay'
    altered_word = f'{mo_vowels.group()}{suffix}'

    return altered_word


def main():
    """Entry point."""
    # TODO: Draft input section.
    # text = 'My name is AL SWEIGART and I am 4,000 years old.'
    text = 'character'
    pig_latin = []

    for word in text.split():
        if re.search('[a-zA-Z]+', word):
            if re.match('[aeiouAEIOU]', word):
                pig_latin.append(start_with_vowel(word))
            else:
                pig_latin.append(start_with_consonant(word))
        else:
            pig_latin.append(word)

    pig_latin[0] = pig_latin[0].capitalize()
    print(' '.join(pig_latin))


if __name__ == '__main__':
    main()
