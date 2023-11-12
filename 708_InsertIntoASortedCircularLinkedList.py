#https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/

from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        new_node = Node(insertVal)

        if head is None:
            new_node.next = new_node
            return new_node
        
        current_node = head
        while True:
            if current_node.val <= current_node.next.val:
                # increasing trend
                if current_node.next == head or (insertVal >= current_node.val and insertVal <= current_node.next.val):
                    # insert in between
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return head
                    
            else:
                # decreasing trend
                if insertVal >= current_node.val or insertVal <= current_node.next.val :
                    # insert in between
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return head

            current_node = current_node.next