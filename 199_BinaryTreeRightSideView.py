#https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from collections import deque
from typing import Optional
import math
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        prev_height = -math.inf
        prev_val = None
        vals = []
        to_explore = deque([(root, 0)])
        while to_explore:
            current_node, current_height = to_explore.popleft()
            if prev_height < current_height:
                if prev_val is not None:
                    vals.append(prev_val)
                prev_height = current_height
            prev_val = current_node.val
            if current_node.left:
                to_explore.append([current_node.left, current_height+1])
            if current_node.right:
                to_explore.append([current_node.right, current_height+1])
        vals.append(prev_val)
        return vals


    def leftSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        prev_height = -math.inf
        vals = []
        to_explore = deque([(root, 0)])
        while to_explore:
            current_node, current_height = to_explore.popleft()
            if prev_height < current_height:
                vals.append(current_node.val)
                prev_height = current_height
            if current_node.left:
                to_explore.append([current_node.left, current_height+1])
            if current_node.right:
                to_explore.append([current_node.right, current_height+1])
        return vals
      

        