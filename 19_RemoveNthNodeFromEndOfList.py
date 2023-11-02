#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n <=0:
            raise ValueError(f"invalid n = {n}")
        
        if head is None:
            return None

        zero_node = ListNode()
        zero_node.next = head

        # move the first pointer to the n-th node
        first = zero_node
        pos = 0
        while first.next and pos < n:
            pos += 1
            first = first.next

        if pos < n:
            raise ValueError(f"Linked list is too short of length {pos} compared to n={n}")
        
        second = zero_node

        # move both pointers till first reaches the end of the list
        while first.next:
            first = first.next
            second = second.next
        
        # remove the node next to second
        second.next = second.next.next

        # return the next node of zero node
        return zero_node.next


    def removeNthFromEndTwoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n <=0:
            raise ValueError(f"invalid n = {n}")
        
        if head is None:
            return None

        # find length of linked list
        current_node = head
        length = 1
        while current_node.next:
            current_node = current_node.next
            length += 1

        # length : 1 , length-1:2, ... length-n+1:n

        if n == length:
            return head.next
        elif length-n+1 >0 and length-n+1<= length:
            # remove length - n + 1 th node if it exists

            # walk to length-n th node 
            current_node = head
            pos = 1
            while current_node.next and pos < length-n:
                current_node = current_node.next
                pos += 1

            current_node.next = current_node.next.next

        return head
