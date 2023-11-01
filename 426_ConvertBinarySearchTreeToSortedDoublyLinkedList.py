#https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

from typing import Optional

#Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convert_subtree(self, root: 'Node') -> tuple['Node', 'Node']:
        if root.left:
            left_min, left_max = self.convert_subtree(root.left)
        if root.right:
            right_min, right_max = self.convert_subtree(root.right)
        
        current_min = root
        current_max = root

        if root.left:
            left_max.right = root
            root.left = left_max
            current_min = left_min
        
        if root.right:
            root.right = right_min
            right_min.left = root
            current_max = right_max

        return current_min, current_max
        

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        min_node, max_node = self.convert_subtree(root)

        # leetcode wanted a singleton to doubly link to itself :/
        #if min_node != max_node:
        #    max_node.right = min_node
        #    min_node.left = max_node

        max_node.right = min_node
        min_node.left = max_node
        return min_node

