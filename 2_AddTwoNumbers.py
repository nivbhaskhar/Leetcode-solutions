#https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            if carry == 0:
                answer = None
            else:
                answer = ListNode(carry)
        elif l1 is None and l2 is not None:
            new_carry, new_residue = self.getCarryResidue(carry + l2.val)
            answer = ListNode(new_residue)
            answer.next = self.addRecursive(l1, l2.next, new_carry)
        elif l1 is not None and l2 is None:
            new_carry, new_residue = self.getCarryResidue(carry + l1.val)
            answer = ListNode(new_residue)
            answer.next = self.addRecursive(l1.next, l2, new_carry)
        elif l1 is not None and l2 is not None:
            new_carry, new_residue =  self.getCarryResidue(carry + l1.val + l2.val)
            answer = ListNode(new_residue)
            answer.next = self.addRecursive(l1.next, l2.next, new_carry)
        return answer

		
    


    def getCarryResidue(self, num: int)-> tuple[int, int]:
        residue = num % 10
        carry = (num-residue)//10
        return (carry, residue)
            

            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addRecursive(l1, l2, 0)
        


