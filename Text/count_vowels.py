#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import sys


def count_vowels(str):
    """
    Count Vowels - Enter a string and the program counts 
    the number of vowels in the text. For added complexity have it 
    report a sum of each vowel found.

    >>> count_vowels('foo')
    {'o': 2}
    >>> count_vowels('')
    {}
    >>> count_vowels('djkstr rllz')
    {}
    """
    char_counts = Counter(str)
    vowels = {key: char_counts[key]
              for key in char_counts.keys() if key in 'aoeuiy'}
    return vowels          


def test_count_vowels():
    '''
    pytest for function count_vowels()
    count_vowels should get string and return dictionary { vowel: count}
    for empty string should return empty dict
    '''
    assert count_vowels('foo bar') == {'o': 2, 'a': 1}
    assert count_vowels('lorem ipsum') == {'o': 1, 'e': 1, 'u': 1, 'i': 1}
    assert count_vowels('') == {}
    assert count_vowels('djkstr rllz') == {}

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    #print(count_vowels(input()))
    data = sys.stdin.readlines()
    print(count_vowels(''.join(data)))