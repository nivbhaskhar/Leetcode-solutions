#https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
from collections import deque, defaultdict
from typing import Optional
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None: 
            return []
        
        max_depth = -math.inf
        column_view = defaultdict(list)
        to_explore = deque([(root, 0, 0)]) # (node, level, col)
        while to_explore:
            current_node, current_depth, current_col = to_explore.popleft()
            max_depth = max(max_depth, current_depth)
            column_view[current_col].append(current_node.val)
            if current_node.left:
                to_explore.append((current_node.left, current_depth+1, current_col-1))
            if current_node.right:
                to_explore.append((current_node.right, current_depth+1, current_col+1))
    
        vertical_ordering = []
        for d in range(-max_depth,max_depth+1):
            if d in column_view:
                vertical_ordering.append(column_view[d])
        return vertical_ordering