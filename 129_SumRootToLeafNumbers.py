#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: TreeNode, digits_seen: list[str])->int:
        """
        returns sum at leaf nodes in subtree at node
        """
        digits_seen.append(str(node.val))

        if node.left is None and node.right is None:
            #print(''.join(digits_seen))
            ans = int(''.join(digits_seen))
            digits_seen.pop()
            return ans
        
        left_ans = 0
        right_ans = 0
        if node.left:
            left_ans = self.dfs(node.left, digits_seen)
            #print(f"left_ans = {left_ans}")
        if node.right:
            right_ans = self.dfs(node.right, digits_seen)
            #print(f"right_ans = {right_ans}")

        digits_seen.pop()
        return left_ans + right_ans




    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root, [])
