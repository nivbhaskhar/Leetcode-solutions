#https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description/

class Solution:
    def get_int(self, expression:str)->int:
        if expression:
            return int(expression)
        else:
            return 1
        
    def eval(self, left_factor: str, right_factor: str, left_summand: str, right_summand:str)->int:
        summand = self.get_int(left_summand)+self.get_int(right_summand)
        factor = self.get_int(left_factor)*self.get_int(right_factor)
        return summand*factor
    def minimizeResult(self, expression: str) -> str:
        val = math.inf
        bracketed_expression = None
        n = len(expression)
        plus_pos = expression.index("+")
        for left_bracket_pos in range(plus_pos):
            #left_bracket is at x if (expression[x]
            for right_bracket_pos in range(plus_pos+1,n):
                #right_bracket is at x if expression[x])
                left_factor = expression[:left_bracket_pos]
                right_factor = expression[right_bracket_pos+1:]
                left_summand = expression[left_bracket_pos:plus_pos]
                right_summand = expression[plus_pos+1:right_bracket_pos+1]
                new_val = self.eval(left_factor,right_factor,left_summand, right_summand)
                if val > new_val:
                    bracketed_expression = left_factor+"("+left_summand+"+"+right_summand+")"+right_factor
                    val = new_val

        return bracketed_expression
