#https://leetcode.com/problems/sort-colors/


#Straight-forward two pass solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Given a list of numbers from {0,1,2}, sorts them in ascending order
        Does not return anything, modifies nums in-place instead.
        """
        freq = [0,0,0]
        for i in nums:
            freq[i] +=1
            
        j = 0
        for label, i in enumerate(freq):
            count = 0
            while(count < i):
                nums[j] = label
                j += 1
                count += 1
                
        
        # Complexity analysis 
        #n = length of nums
        # Time complexity O(n)
        # Two passes of nums

    #One pass solution
    def sortColors_upgrade(self, nums: List[int]) -> None:
        """
        Given a list of numbers from {0,1,2}, sorts them in ascending order
        Does not return anything, modifies nums in-place instead.
        """
        #[0:low] all 0
        #[low:mid] all 1
        #[mid:high+1] unknowns
        #[high+1:] all 2

        low = 0
        mid = 0
        high = len(nums)-1
        #initially all elements of array are in unknown range
        
        while(mid <= high):
            if nums[mid]==0:
                #swap nums[mid] and nums[low]
                #increment low, mid
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                #increment mid
                mid += 1

            else:
                #nums[mid]=2 therefore
                #swap nums[mid] and nums[high]
                #decrement high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
    
  
                
        




