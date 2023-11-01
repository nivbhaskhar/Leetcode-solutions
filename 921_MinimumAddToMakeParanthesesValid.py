#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_moves = 0
        num_open_brackets = 0
        for bracket in s:
            if bracket == "(":
                num_open_brackets += 1
            elif bracket == ")":
                if num_open_brackets > 0:
                    num_open_brackets -=1
                else:
                    num_moves += 1
            else:
                raise ValueError(f"invalid character {bracket} found")
        
        return num_moves + num_open_brackets
        
            

  