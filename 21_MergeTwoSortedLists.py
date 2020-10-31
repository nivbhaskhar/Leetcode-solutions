#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        pointer_1 = l1
        pointer_2 = l2
        current_node = root
        while(pointer_1 is not None or pointer_2 is not None):
            current_node.next = ListNode(0)
            current_node = current_node.next
            val_1 = math.inf
            val_2 = math.inf
            if pointer_1 is not None:
                    val_1 = pointer_1.val
            if pointer_2 is not None:
                     val_2 = pointer_2.val 
            if val_1 <= val_2:
                    current_node.val = val_1
                    pointer_1 = pointer_1.next
            else:
                    current_node.val = val_2
                    pointer_2 = pointer_2.next



        return root.next
        
# Complexity analysis
#O(sum of sizes of linked lists)
