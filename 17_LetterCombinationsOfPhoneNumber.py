#https://leetcode.com/problems/letter-combinations-of-a-phone-number/



#Recursion
from collections import defaultdict
class Solution:

    from collections import defaultdict
class Solution:
    def mapDigitsToLetters(self)->dict[int, list[str]]:
        mapping = defaultdict(list)
        number_rep = ord('a')
        distribution = [3,3,3,3,3,4,3,4]
        for j in range(2,10):
            for i in range(distribution[j-2]):
                mapping[str(j)].append(chr(number_rep))
                number_rep += 1
        return mapping

    def letterCombinationsRecursive(self, start_pos: int, digits: list[str], mapping: dict[int, list[str]]) -> List[List[str]]:
        print(start_pos, digits)
        candidate_characters = mapping[digits[start_pos]]
        if start_pos == len(digits)-1:
            return [[character] for character in candidate_characters]
        
        prev_combinations = self.letterCombinationsRecursive(start_pos+1, digits, mapping)
        new_combinations = []
        for character in candidate_characters:
            for combination in prev_combinations:
                new_combination = combination.copy()
                new_combination.append(character)
                new_combinations.append(new_combination)
        return new_combinations
        
        
        


    def letterCombinations(self, digits: str) -> list[str]:
        mapping = self.mapDigitsToLetters()
        if len(digits) == 0:
            return []
        list_of_digits = [d for d in digits]
        return [''.join(reversed(x)) for x in self.letterCombinationsRecursive(0, list_of_digits, mapping)]
    

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


    def letterCombinationsOld(self, digits: str, rec=False) -> list[str]:
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

  
