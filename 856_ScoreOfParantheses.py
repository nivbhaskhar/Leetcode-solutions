# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        if len(s) == 0:
            return 0

        processing_stack = []
        for i, character in enumerate(s):
            if character == "(":
                processing_stack.append(character)
            elif character == ")":
                temp_score = 0
                while len(processing_stack) > 0 and processing_stack[-1] != "(":
                    s = processing_stack.pop()
                    temp_score += s
                if len(processing_stack) == 0:
                    raise ValueError(f"string {s} is not balanced, closing bracket at pos {i} has no corresponding opening bracket")
                else:
                    assert processing_stack[-1] == "("
                    processing_stack.pop()
                    if temp_score == 0:
                        processing_stack.append(1)
                    else:
                        processing_stack.append(2*temp_score)
            else:
                raise ValueError(f"spotted invalid character {character} as position {i}")
            
        return sum(processing_stack)

# Complexity O(n)