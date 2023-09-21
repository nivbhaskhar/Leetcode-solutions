#https://leetcode.com/problems/happy-students/
from collections import deque
class Solution:
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        nums = deque(nums)
        processed = []
        num_ways = 0
        for num_students_picked in range(len(nums)+1):
            reject_num_students_picked = False
            while nums and num_students_picked >= nums[0]:
                elem = nums.popleft()
                processed.append(elem)
                if elem == num_students_picked:
                    reject_num_students_picked = True
            if reject_num_students_picked is False:
                if len(processed) == num_students_picked:
                    num_ways +=1
        return num_ways