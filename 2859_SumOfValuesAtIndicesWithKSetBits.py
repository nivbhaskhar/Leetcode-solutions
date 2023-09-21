#https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
class Solution:
    
    def bit_count(self, num: int)->int:
        count = 0
        while num:
            count += num & 1 #gets least significant bit
            num >>= 1 # chops off least significant bit in num bin rep
        return count
    
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        #return sum([nums[x] for x in range(len(nums)) if x.bit_count() == k])
        return sum([nums[x] for x in range(len(nums)) if self.bit_count(x) == k]) # built in method
    