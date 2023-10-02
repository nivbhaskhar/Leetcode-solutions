#https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        k=0
        prev_node = None
        current_node = head
        left_cut = None
        left_node = None
        right_node = None
        right_cut = None
        while(current_node and k < right):
            k += 1
            if k < left:
                left_cut = current_node
            if k == left:
                left_node = current_node
            if k == right:
                right_node = current_node
                right_cut = current_node.next
            next_node = current_node.next
            if k == left:
                current_node.next = None
            elif k > left and k<= right:
                current_node.next = prev_node
            prev_node = current_node 
            current_node = next_node
        

        if left_cut is not None:
            left_cut.next = right_node
        if left_node is not None:
            left_node.next = right_cut

        if left_cut is not None:
            return head
        else:
            return right_node