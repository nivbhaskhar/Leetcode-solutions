#https://leetcode.com/problems/random-pick-with-weight/description/
import random
class Solution:

    def __init__(self, w: list[int]):
        self.total = sum(w)
        self.len = len(w)
        self.cumulative_sum = [0]*self.len
        sum_of_wts = 0
        for pos, wt in enumerate(w):
            sum_of_wts += wt
            self.cumulative_sum[pos] = sum_of_wts


    def pickIndex(self) -> int:
        r = random.uniform(0, 1)
        val = self.total*r

        # in self.cumulative_sum = [v0,v1,...,v_(n-1)], search for v_i so that 
        # it is the min number >= val

        start = 0
        end = self.len-1
        while(start < end-1):
            mid = (start + end)//2
            if self.cumulative_sum[mid] < val:
                start = mid
            else:
                end = mid
        
        if self.cumulative_sum[start] >= val:
            return start
        else:
            return end



        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()