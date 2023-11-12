#https://leetcode.com/problems/maximum-swap/description/
from collections import deque
class Solution:
    def get_num(self, digits:list[int])->int:
        ans = 0
        for digit in digits:
            ans = (10*ans) + digit
        return ans 

    def get_digits(self, num:int) -> list[int]:
        digits = []
        if num == 0:
            return [0]

        while num !=0:
            d = num % 10
            digits.append(d)
            num = num//10
        return list(reversed(digits))

    def maximumSwap(self, num: int) -> int:
        if num == 0:
            return 0
        
        digits = self.get_digits(num)
        digit_last_position = defaultdict(int)
        for i, digit in enumerate(digits):
            digit_last_position[digit] = max(i, digit_last_position[digit])

        #print(f"digits = {digits}")
        #print(f"digit positions = {digit_positions}")



        sorted_digits = sorted(digits, reverse = True)
        #print(f"sorted digits = {sorted_digits}")
        
        for i, digit in enumerate(digits):
            max_digit = sorted_digits[i]
            if max_digit != digit:
                max_pos = digit_last_position[max_digit]
                digits[i] = max_digit
                digits[max_pos] = digit
                break
            #else:
            #    digit_positions[digit].popleft()
        
        #print(f"ans digits = {digits}")
        return self.get_num(digits)

