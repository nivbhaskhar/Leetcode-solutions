#https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        winning_pos = (0,0)
        max_length = 1
        n = len(s)
        prev_is_palindrome = {0: True}
        for end in range(1,n):
            curr_is_palindrome = {}
            for start in range(end+1):
                if start == end:
                    curr_is_palindrome[start] = True
                elif start == end-1:
                    curr_is_palindrome[start] = (s[start]==s[end])
                else:
                    curr_is_palindrome[start] = (s[start]==s[end]) & (prev_is_palindrome[start+1])
                if curr_is_palindrome[start] and (end-start+1 > max_length):
                    max_length = end-start+1
                    winning_pos = (start, end)
            prev_is_palindrome = curr_is_palindrome
        return s[winning_pos[0]:winning_pos[1]+1]




