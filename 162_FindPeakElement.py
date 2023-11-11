#https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)

        start = 0
        end = n-1

        while(start<end-1):
            mid = (start + end)//2 #(1+3)//2 = 2, (1+4)//2 = 2
            if nums[mid] < nums[mid+1]:
                start=mid
            elif nums[mid-1]>nums[mid]:
                end = mid
            else:
                return mid 

    
        if start == end:
            return start
        else:
            assert start == end-1, f"{start},{end} not consecutive"
            if nums[start] > nums[end]:
                return start
            else:
                return end

        
        