#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos_of_nums = {}
        for pos,num in enumerate(nums):
            if num in pos_of_nums:
                if target == 2*num:
                    return [pos_of_nums[num], pos]
            pos_of_nums[num] = pos
            complement = target - num
            if complement in pos_of_nums and pos_of_nums[complement] != pos:
                return [pos, pos_of_nums[complement]]