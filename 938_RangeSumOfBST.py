#https://leetcode.com/problems/range-sum-of-bst/description/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        ans = root.val
        left_sum = 0
        right_sum = 0

        if root.val <= low:
            if root.val < low:
                ans = 0
            if root.right:
                right_sum = self.rangeSumBST(root.right, low, high)
        elif root.val >= high:
            if root.val > high:
                ans = 0
            if root.left:
                left_sum = self.rangeSumBST(root.left, low, high)
        else:
            if root.left:
                left_sum = self.rangeSumBST(root.left, low, root.val)
            if root.right:
                right_sum = self.rangeSumBST(root.right, root.val, high)
        return ans + left_sum + right_sum
            

        