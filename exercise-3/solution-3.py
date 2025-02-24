# -*- coding:utf-8 -*-

import unittest


def get_concatenation(nums):
    pass


class TestGetConcatenation(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(get_concatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])
        self.assertEqual(get_concatenation(
            [1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])

    def test_empty_list(self):
        self.assertEqual(get_concatenation([]), [])

    def test_single_element(self):
        self.assertEqual(get_concatenation([5]), [5, 5])

    def test_large_list(self):
        nums = list(range(1000))
        expected = nums + nums
        self.assertEqual(get_concatenation(nums), expected)


if __name__ == "__main__":
    unittest.main()
