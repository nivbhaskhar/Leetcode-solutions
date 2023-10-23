#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        processing_stack = []
        for pos, char in enumerate(s):
            if char == ")":
                if processing_stack:
                    processing_stack.pop()
                else:
                    to_remove.add(pos)
            elif char == "(":
                processing_stack.append(pos)

        for pos in processing_stack:
            to_remove.add(pos)
        
        return ''.join([s[pos] for pos in range(len(s)) if pos not in to_remove])