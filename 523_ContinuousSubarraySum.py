#https://leetcode.com/problems/continuous-subarray-sum/description/
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        if len(nums) <= 1:
            return False

        current_sum = 0
        prefix_sums_to_positions = defaultdict(list)
        for i, num in enumerate(nums):
            current_sum += num
            current_sum = current_sum % k
            prefix_sums_to_positions[current_sum].append(i)
        
        if len(prefix_sums_to_positions[0]) >= 1 and prefix_sums_to_positions[0][-1] > 0:
            return True
        
        for prefix_sum, positions in prefix_sums_to_positions.items():
            if len(positions)>=2 and positions[-1]-positions[0] >=2:
                return True
        
        return False



        










