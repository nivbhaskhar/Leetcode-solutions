#https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def get_stats_of_subtree(self, node: TreeNode)->tuple[int,int,int]:
        if node.left:
            left_sum, left_num_nodes, left_ans = self.get_stats_of_subtree(node.left)
        else:
            left_sum, left_num_nodes, left_ans = 0,0,0
        
        if node.right:
            right_sum, right_num_nodes, right_ans = self.get_stats_of_subtree(node.right)
        else:
            right_sum, right_num_nodes, right_ans = 0,0,0

        curr_sum = left_sum + right_sum + node.val
        curr_num_nodes = left_num_nodes + right_num_nodes + 1
        curr_ans = left_ans + right_ans
        if curr_sum//curr_num_nodes == node.val:
            #print(f"adding node {node.val}")
            curr_ans += 1
        
        return curr_sum, curr_num_nodes, curr_ans

        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.get_stats_of_subtree(root)[2]


