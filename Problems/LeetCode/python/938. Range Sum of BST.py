# 938. Range Sum of BST
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    given root of bst, return sum of values in [low, high]
    1st attempt: simple dfs O(n + (n - 1)) = O(n), use list since import queue unavailable
    """
    def range_sum_bst(self, root: TreeNode, low: int, high: int) -> int:
        """
        Complexity:
        Time: O(n) DFS on BST
        Space: O(n)
        LeetCode results
        Runtime: 196 ms
        Memory: 22.3 MB
        """
        self.rsum = 0
        # Prevent having to pass in low, high and return rsum for each iteration.
        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.rsum += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        dfs(root)
        return self.rsum


