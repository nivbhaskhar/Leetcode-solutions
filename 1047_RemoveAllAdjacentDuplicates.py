#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack_of_characters = ['']
        for character in S:
            if character == stack_of_characters[-1]:
                stack_of_characters.pop()
            else:
                stack_of_characters.append(character)

        return ''.join(stack_of_characters)

#Complexity analysis
#O(len(S))
        
        
     def removeDuplicates_inefficient(self, S: str) -> str:
         n = len(S)
         del_pos = None
         for i in range(n-1):
             if S[i]==S[i+1]:
                 del_pos = i
                 break
         if del_pos is None:
             return S
         else:
             S_prime = S[:i]+S[i+2:]
             return self.removeDuplicates(S_prime)
            
#Complexity analysis
#O(len(S)^2)
