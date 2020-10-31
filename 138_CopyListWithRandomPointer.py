#https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        old_to_new_dict = {None:None}
        root = Node(0,None,None)
        current_node_in_new_list = root
        current_node_in_given_list = head
        while(current_node_in_given_list):
            val = current_node_in_given_list.val
            random_pointer = current_node_in_given_list.random
            current_node_in_new_list.next = Node(val, None, random_pointer)
            current_node_in_new_list = current_node_in_new_list.next
            old_to_new_dict[current_node_in_given_list] = current_node_in_new_list
            current_node_in_given_list = current_node_in_given_list.next

            
        current_node_in_new_list = root.next
        while(current_node_in_new_list):
            random_pointer = current_node_in_new_list.random
            current_node_in_new_list.random = old_to_new_dict[random_pointer]
            current_node_in_new_list = current_node_in_new_list.next
        
        return root.next
        
