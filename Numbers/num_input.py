#! /usr/bin/env python
# -*- coding: utf-8 -*-

def input_int(prompt = 'Enter a number: '):
    '''
    input function to get int values from stdin
    '''
    while True:
        num_str = input(prompt).strip()
        if all(c in '+0123456789' for c in num_str):
            break
    return int(num_str)