#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def update_parents_dfs(self, node: 'TreeNode'):
        if node.left:
            self.update_parents(node.left)
            node.left.parent = node
        if node.right:
            self.update_parents(node.right)
            node.right.parent = node
        
    def update_parents(self, root:'TreeNode'):
        root.parent = None
        to_explore = deque([root])
        while to_explore:
            current_node = to_explore.popleft()
            if current_node.left:
                current_node.left.parent = current_node
                to_explore.append(current_node.left)
            if current_node.right:
                current_node.right.parent = current_node
                to_explore.append(current_node.right)





    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root.parent = None
        self.update_parents(root)

        # walk up to root from p
        current_node = p
        ancestors_of_p = set()
        while current_node:
            ancestors_of_p.add(current_node)
            current_node = current_node.parent
        
        # walk up from q till you get some ancestor of p
        current_node = q
        while current_node and current_node not in ancestors_of_p:
            current_node = current_node.parent
        
        return current_node

