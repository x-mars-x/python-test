# -*- coding:utf-8 -*-

import unittest


def getConcatenation(nums):
    len_n = len(nums)
    res = [0]*2*len_n
    for i in range(len(res)):
        if i >= len_n:
            res[i] = nums[i-len_n]
        else:
            res[i] = nums[i]
    return res


nums = [1, 2, 1]


print(getConcatenation(nums))
