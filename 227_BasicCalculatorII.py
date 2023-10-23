#https://leetcode.com/problems/basic-calculator-ii/description/

from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        s+= "+"
        operators = set(["+", "-", "*", "/"])
        actions = {"*": lambda x,y: x*y, "+": lambda x,y: x+y, "/":lambda x,y: x//y, "-": lambda x,y: x-y}
        mult_operators = set(["*", "/"])
        add_operators = set(["+", "-"])
        digits = set([str(i) for i in range(10)])
        current_number_digits = []
        processing_stack = deque([])
        for character in s:
            if character == " ":
                continue
            elif character in digits:
                current_number_digits.append(character)
            elif character in operators:
                current_number = int(''.join(current_number_digits))
                current_number_digits = []
                if processing_stack and processing_stack[-1] in mult_operators:
                    assert len(processing_stack)>=2, f"invalid expression {s}"
                    prev_operator = processing_stack.pop()
                    prev_number = processing_stack.pop()
                    evaluated_number = actions[prev_operator](prev_number, current_number)
                    processing_stack.append(evaluated_number)
                else:
                    processing_stack.append(current_number)
                processing_stack.append(character)
            else:
                raise ValueError(f"invalid character {character} in {s}")
        if current_number_digits:
            processing_stack.append(int(''.join(current_number_digits)))
        
        assert processing_stack[-1] == "+", f"something went wrong 3 {processing_stack}"
        processing_stack.pop()
        if len(processing_stack) == 0:
            return 0
        
        #print(processing_stack)
        ans = processing_stack.popleft()
        assert isinstance(ans, int), f"something went wrong1 {processing_stack}"
        while processing_stack:
            v = processing_stack.popleft()
            if v in operators:
                assert v in add_operators, f"something went wrong {processing_stack}"
                val =  processing_stack.popleft()
                ans = actions[v](ans, val)

        return ans
