#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt
import unittest
from num_input import input_int


def nth_fibonacci(n):
    '''
    calculate nth number of Fibonacci sequence by using Binet's formula.
    '''
    golden_ratio = (1 + sqrt(5)) / 2.0
    copper_ratio = (1 - sqrt(5)) / 2.0  # just kidding
    fib_nth = (golden_ratio ** n - copper_ratio ** n) / sqrt(5)
    return int(fib_nth)


class NthFibonacciTestCase(unittest.TestCase):

    def setUp(self):
        self.fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                          144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

    def test_fibonacci_numbers(self):
        # make sure nth_fibonacci() correct calculates first ~20 fibonacci
        # values
        for index, value in enumerate(self.fibonacci):
            self.assertEqual(value, nth_fibonacci(index))

if __name__ == '__main__':
    # unittest.main()
    n = input_int('Enter index in fibonacci sequence: ')
    fib_n = nth_fibonacci(n)
    print("{}th number fibonacci is {}".format(n, fib_n))
