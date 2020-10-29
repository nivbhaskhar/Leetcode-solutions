#https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        visited = {root: 0}
        current_level = 0
        list_of_all_level_lists = []
        current_level_list = []
        to_be_explored = deque([root])
        while to_be_explored:
            current_vertex = to_be_explored.popleft()
            if visited[current_vertex] == current_level:
                current_level_list.append(current_vertex.val)
            else:
                list_of_all_level_lists.append(current_level_list)
                current_level = visited[current_vertex]
                current_level_list = [current_vertex.val]
            if current_vertex.left is not None and current_vertex.left not in visited:
                visited[current_vertex.left] = current_level + 1
                to_be_explored.append(current_vertex.left)
            if current_vertex.right is not None and current_vertex.right not in visited:
                visited[current_vertex.right] = current_level + 1
                to_be_explored.append(current_vertex.right)
        
        list_of_all_level_lists.append(current_level_list)       
        return list_of_all_level_lists        
            
                
                
#Complexity analysis
#BFS
        
        
