#https://leetcode.com/problems/letter-combinations-of-a-phone-number/


#Recursion
from collections import defaultdict
class Solution:
    def __init__(self):
        #Dictionary mapping numbers to letters
        self.d = defaultdict(list)
        x = ord('a')
        s = [3,3,3,3,3,4,3,4]
        for j in range(2,10):
               for i in range(s[j-2]):                
                   c = chr(x)
                   self.d[str(j)].append(c)
                   x += 1


    def letterCombinations(self, digits: str, rec=False) -> list[str]:
        if not digits and rec:
            return ['']
        elif not digits:
            return []
        else:
            l = self.letterCombinations(digits[1:], True)
            ans_list = []
            for elem in l:
                for character in self.d[digits[0]]:
                    ans_list.append(character+elem)
            return ans_list


                
# Complexity analysis 
#n = length of input number-string
# output list L of an n-1 length input has size <= 4^(n-1)
# Each element in L is a string of length n-1
#concatenating each letter from {x_1,x_2,x_3,x_4} to every element of L => O(4^n) concatentations
# Each concatenation is O(n)

# f(n) = f(n-1) + O(n4^n)

# f(n) = (n)4^n + (n-1)4^(n-1) + .... = O(4^n)

# Time complexity O(4^n)

  
