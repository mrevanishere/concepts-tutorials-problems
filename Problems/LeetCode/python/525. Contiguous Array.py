# 525. Contiguous Array
"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""


def find_max_length_naive(nums: list) -> int:
    max = 0
    for i in range(len(nums)):
        zeros, ones = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                max = max(max, j - i + 1)
    return max


# class Solution(object):
#     def findMaxLength(self, nums):
#         count = 0
#         max_length = 0
#         table = {0: 0}
#         for index, num in enumerate(nums, 1):
#             if num == 0:
#                 count -= 1
#             else:
#                 count += 1
#
#             if count in table:
#                 max_length = max(max_length, index - table[count])
#             else:
#                 table[count] = index
#
#         return max_length