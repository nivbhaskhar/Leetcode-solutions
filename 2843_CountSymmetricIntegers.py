# https://leetcode.com/problems/count-symmetric-integers/

import math

class Solution:
    # def numDigits(self, x: int)->int:
    #     if x == 0:
    #         digits = 1
    #     else:
    #         digits = int(math.log10(abs(x)))+1
    #     return digits 
    
    def getDigits(self, x: int)->list[int]:
        if x == 0:
            return [0]
        else:
            digits = []
            while x > 0:
                digit = x % 10
                x = x//10
                digits.append(digit)
        return digits  
    
    def isSymmetric(self, x: int)->bool:
        digits = self.getDigits(x)
        l = len(digits)
        if l % 2 == 1:
            return False
        else:
            s = 0
            t = 0
            for i in range(l):
                if i < l//2:
                    s += digits[i]
                else:
                    t += digits[i]
            return s == t
                    
            
        
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum([self.isSymmetric(x) for x in range(low, high+1)])
        