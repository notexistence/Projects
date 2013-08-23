#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse_string(str):
    """Reverse string.

    >>> reverse_string('bar')
    'rab'
    >>> reverse_string('lorem ipsum')
    'muspi merol'
    """
    return str[::-1]


def test_solution():
    '''
    pytest for check solution.
    To run test run from console: py.test module_name.py
    '''
    assert reverse_string('foo') == 'oof'
    assert reverse_string('') == ''
    assert reverse_string(' ') == ' '
    assert reverse_string('lorem ipsum') == "muspi merol"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    usr_str = input('Enter string to reverse: ')
    print("You say '{}', i'm say '{}'".format(
        usr_str, reverse_string(usr_str)))