#https://leetcode.com/problems/3sum-closest/
import math
class Solution:
    def twoSumClosest(self, target: int, nums: list[int], start: int)->int:
        n = len(nums)
        start = start+1
        end = n-1
        difference = math.inf # min abs(target-candidate_sum)
        if start >= end:
            raise ValueError(f"invalid start = {start} and end = {end}")
        two_sum = 0
        while(start < end):
            current_sum = nums[start] + nums[end]
            current_difference = abs(current_sum - target)
            if current_sum > target:
                end -= 1
            elif current_sum < target:
                start += 1
            else:
                return current_sum
            if current_difference < difference:
                difference = current_difference
                two_sum = current_sum
        return two_sum

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) <= 2:
            raise ValueError(f"nums has invalid length {len(nums)}")
        nums.sort()
        print(nums)
        difference = math.inf # min abs(target-candidate_sum)
        three_sum = 0
        for pos, x in enumerate(nums):
            if pos < len(nums)-2:
                two_sum = self.twoSumClosest(target-x, nums, pos)
                current_sum = x + two_sum
                current_difference = abs(target-current_sum)
                if difference > current_difference:
                    difference = current_difference
                    three_sum = current_sum
                    
        return three_sum