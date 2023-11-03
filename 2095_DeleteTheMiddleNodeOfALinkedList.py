#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddleTwoPass(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        length = 1
        current_node = head
        while current_node.next:
            current_node = current_node.next
            length += 1

        # walk to length//2 th node
        mid = length//2
        pos = 1
        current_node = head
        while (pos < mid):
            current_node = current_node.next
            pos += 1
        
        current_node.next = current_node.next.next
        return head


    def deleteMiddleOnePass(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        zero_node = ListNode()
        zero_node.next = head

        fast_pointer = head
        slow_pointer = zero_node
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            if fast_pointer.next:
                fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        
        slow_pointer.next = slow_pointer.next.next
        return zero_node.next