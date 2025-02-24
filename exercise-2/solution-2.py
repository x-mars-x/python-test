# -*- coding:utf-8 -*-

import unittest


def find_smallest_number(n, t):
    """
    :type n: int
    :type t: int
    :rtype: int
    """
    pass


class TestSmallestValidNumber(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_smallest_number(10, 2), 10)
        self.assertEqual(find_smallest_number(15, 3), 16)
        self.assertEqual(find_smallest_number(7, 5), 10)
        self.assertEqual(find_smallest_number(23, 4), 24)
        self.assertEqual(find_smallest_number(99, 6), 100)


if __name__ == "__main__":
    unittest.main()
