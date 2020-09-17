#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        tortoise = head
        hare = head
        while(hare is not None and tortoise is not None):
                tortoise = tortoise.next
                if hare.next:
                    hare = hare.next.next
                else:
                    return False
                if tortoise==hare:
                    return True
        return False


Space Complexity analysis
-------------------------
O(1)

Time Complexity analysis
-------------------
n = number of nodes in linked list
If no cycle, each pointer traverses the list once - O(n)
If cycle, once pointers enter the cycle, tortoise is moving at speed 1 unit/step and hare at 2 units/step. Relative speeds are 0 and 1 respectively. So Hare will meet tortoise eventually (think of tortoise staying put and hare moving in circle)



Or if cycle has length k, label vertices 0,1...k-1.
Assume tortoise at pos 0 and hare at pos non-zero s
In t steps, tortoise would be at t mod k
Hare would be at s+2t mod k
Want s+2t = t mod k
Want s = -t mod k

s < k
t = k-s

in k-s steps, tortoise would be at k-s and hare at s + 2(k-s) = 2k-s = k-s mod k

So O(n) again





