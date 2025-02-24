# -*- coding:utf-8 -*-

import unittest


def fizz_buzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    pass

class TestFizzBuzz(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(fizz_buzz(3), ["1", "2", "Fizz"])

    def test_case_2(self):
        self.assertEqual(fizz_buzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_case_3(self):
        self.assertEqual(fizz_buzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

    def test_case_4(self):  # Edge case: n = 1
        self.assertEqual(fizz_buzz(1), ["1"])

    def test_case_5(self):  # Larger input
        self.assertEqual(fizz_buzz(20), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"])


if __name__ == '__main__':
    unittest.main()