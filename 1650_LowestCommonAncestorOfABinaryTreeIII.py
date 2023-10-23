#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors_of_p = set()

        current_node = p
        while current_node:
            ancestors_of_p.add(current_node.val)
            current_node = current_node.parent
        
        current_node = q
        while current_node:
            if current_node.val in ancestors_of_p:
                return current_node
            current_node = current_node.parent
        
        