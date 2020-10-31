#https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        set_of_words = set(wordDict)
        slices = {}

        def is_concatenated(first_pos, last_pos):
            if (first_pos, last_pos) in slices:
                return slices[(first_pos, last_pos)]
            if first_pos > last_pos:
                slices[(first_pos, last_pos)]=True
                return True
            prefix_list = []
            for pos in range(first_pos,last_pos+1):
                prefix_list.append(s[pos])
                if ''.join(prefix_list) in set_of_words and is_concatenated(pos+1,last_pos):
                     slices[(first_pos, last_pos)]=True 
                     return True
            slices[(first_pos,last_pos)]=False
            return False


        return is_concatenated(0,n-1)


#Complexity : compute is_concatenated for n inputs (last_pos is always n-1)
#For each is_concatenated call -> O(n) # of prefixes worst case, and O(n) for each concatenation of prefix, so it is O(n^2) worst case for each is_concatenated call. So over all O(n^3) complexity
