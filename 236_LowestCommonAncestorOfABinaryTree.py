#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        processing_stack = [(root,0)]
        lca_index = None
        found = {p: False, q:False}
        while processing_stack:
            #print(f"{[(node.val, status) for node, status in processing_stack]}, {lca_index}")
            node, status = processing_stack[-1]
            if node == p or node == q:
                found[node] = True
                num_found = int(found[p]) + int(found[q])
                if num_found == 1:
                    lca_index = len(processing_stack)-1
                    #print(f"lca_val = {processing_stack[lca_index][0].val}")
                elif num_found == 2:
                    break
            
            node, status = processing_stack.pop()

            if status == 0:
                processing_stack.append((node, 1))
                if node.left:
                    processing_stack.append((node.left, 0))
            elif status == 1:
                processing_stack.append((node, 2))
                if node.right:
                    processing_stack.append((node.right, 0))

            if lca_index and lca_index >= len(processing_stack):
                assert lca_index == len(processing_stack)
                lca_index = len(processing_stack)-1
                #print(f"reset lca_val = {processing_stack[lca_index][0].val}")
            
        if found[p] and found[q]:
            return processing_stack[lca_index][0]
        else:
            return None  

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

