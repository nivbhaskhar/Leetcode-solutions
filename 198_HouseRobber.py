#https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        prev_prev_ans = 0
        prev_ans = nums[n-1]
        for i in range(n-2,-1,-1):
            ans = max(prev_ans, nums[i]+prev_prev_ans)
            prev_prev_ans = prev_ans
            prev_ans = ans
            #print(nums[i:], ans)

        
        return ans


        


