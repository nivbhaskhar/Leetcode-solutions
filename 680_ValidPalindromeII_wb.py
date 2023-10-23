#https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def is_palindrome_flexible(self, characters: list[str], start: int, end: int, omissions_left:bool)->bool:
        if start == end:
            return True
        elif start == end-1:
            if characters[start] == characters[end]:
                return True
            elif omissions_left:
                return True
            else:
                return False
        else:
            if characters[start] == characters[end]:
                return self.is_palindrome_flexible(characters, start+1,end-1,omissions_left)
            elif omissions_left:
                skip_start_palindrome = self.is_palindrome_flexible(characters, start+1,end,False)
                skip_end_palindrome = self.is_palindrome_flexible(characters, start,end-1,False)
                return skip_start_palindrome or skip_end_palindrome
            else:
                return False

    def validPalindrome(self, s: str) -> bool:
        if len(s)<= 1:
            return True
        return self.is_palindrome_flexible(list(s), 0, len(s)-1, 1)
        