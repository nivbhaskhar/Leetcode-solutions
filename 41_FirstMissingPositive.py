#https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 0:
            return 1
        
        # preprocessing: reset redundant values < 0 and > N to be 0
        for pos, val in enumerate(nums):
            if val < 0 or val > N:
                nums[pos] = 0
    
        # if you see value val, mark arr[val-1] = -1
        for pos in range(N):
            val = nums[pos]
            while (val >= 1 and val <= N):
                new_val = nums[val-1]
                nums[val-1] = -1
                val = new_val
        
        # walk down the array to detect first missing positive
        ans = N+1
        for pos in range(N):
            if nums[pos] >= 0:
                ans = pos+1
                break

        return ans