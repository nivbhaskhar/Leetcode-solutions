#https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Given an integer, determines if it is a power of two.
        """
        if n <= 0:
            return False
        while(n>1):
            least_significant_bit = (n & 1)
            if least_significant_bit == 1:
                return False
            else:
                n = (n>>1)
        return True
        
        
