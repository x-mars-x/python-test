# -*- coding:utf-8 -*-

import unittest

def find_smallest_number(n, t):
    """
    :type n: int
    :type t: int
    :rtype: int
    """
    while True:
        x = [int(x) for x in str(n)]
        product=1
        for i in x:
            product*=i
        if product % t == 0:
            return n
        n += 1

print(find_smallest_number(7, 5))
print(find_smallest_number(23, 4))
print(find_smallest_number(99, 6))

class TestSmallestValidNumber(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_smallest_number(10, 2), 10) 
        self.assertEqual(find_smallest_number(15, 3), 16) 
        self.assertEqual(find_smallest_number(7, 5), 10)  
        self.assertEqual(find_smallest_number(23, 4), 24) 
        self.assertEqual(find_smallest_number(99, 6), 100)

if __name__ == "__main__":
    unittest.main()
