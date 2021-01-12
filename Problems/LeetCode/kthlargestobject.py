# This way is too slow (sorting everytime)
# needs to have a data structure that is already sorted (heap)
# so turning the arr into a heap is best to keep order while not having to resort

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def merge_sort(self, li):
        if len(li) > 1:
            mid = len(li) // 2
            L = li[:mid]
            R = li[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            # Go through both copies until we run out of elements in one
            while i < len(L) and j < len(R):
                # If our left_copy has the smaller element, put it in the sorted
                # part and then move forward in left_copy (by increasing the pointer)
                if L[i] < R[j]:
                    li[k] = L[i]
                    i += 1
                # Opposite from above
                else:
                    li[k] = R[j]
                    j += 1
                # Regardless of where we got our element from
                # move forward in the sorted part
                k += 1

            # Checking if any element was left
            # We ran out of elements either in left_copy or right_copy
            # so we will go through the remaining elements and add them
            while i < len(L):
                li[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                li[k] = R[j]
                j += 1
                k += 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.merge_sort(self.nums)
        print(self.nums)
        return self.nums[len(self.nums) - 3]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(3, [4, 5, 8, 2])
# print(obj.add(3))
# print(obj.add(5))
