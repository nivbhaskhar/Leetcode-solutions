#https://leetcode.com/problems/longest-substring-without-repeating-characters
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_dict = defaultdict(int)
        longest_window = 0 
        n = len(s)
        start = 0
        end = 0
        while(end < n):
           #window is [start,end]
           #Update freq_dict by newest letter added
           freq_dict[s[end]]+= 1
           if freq_dict[s[end]] > 1:
             #window is invalid
              while(freq_dict[s[end]]>1):
                  freq_dict[s[start]] -= 1
                  start += 1    

           longest_window = max(longest_window, end-start+1)
           end += 1
        return longest_window

#Complexity - O(n)

  
