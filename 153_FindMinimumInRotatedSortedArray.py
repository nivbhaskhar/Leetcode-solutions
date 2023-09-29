#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findArgMax(self, nums:list[int])-> int:
        if len(nums)==1:
            return 0
        start = 0
        end = len(nums)-1
        while(end-start > 1):
            mid = (start + end)//2
            if nums[start] < nums[mid]:
                start = mid
            else:
                end = mid
        
        if nums[start] > nums[end]:
            return start
        else:
            return end        



    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        argmax = self.findArgMax(nums)
        argmin = (argmax+1) % n
        return nums[argmin] 

        