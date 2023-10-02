#https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        while current_node:
            # prev_node | current_node -> next_node
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        return prev_node