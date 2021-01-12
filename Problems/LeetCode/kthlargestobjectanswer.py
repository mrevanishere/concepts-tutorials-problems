# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
