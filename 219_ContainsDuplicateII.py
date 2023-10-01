#https://leetcode.com/problems/contains-duplicate-ii
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums:list[int], k: int) -> bool:
        if k <=0:
            #raise ValueError(f"k = {k} has to be at least 1")
            return False
        if len(nums) <= 1:
            return False
        start = 0
        end = 0
        counter_dict = defaultdict(int)
        while((start <= end) and (end < len(nums))):
            # window [start,.., end] = nums[start:end+1]
            counter_dict[nums[end]] += 1
            if counter_dict[nums[end]] > 1:
                return True
            if end-start == k:
                # move start towards right
                counter_dict[nums[start]] -=1
                start += 1
            end += 1
        return False




    



