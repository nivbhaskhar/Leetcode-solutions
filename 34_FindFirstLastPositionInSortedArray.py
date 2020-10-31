#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def search(start, end, search_for_first):
            if start > end:
                return -1
            elif start==end:
                if nums[start]==target:
                    return start
                else:
                    return -1
            else:
                length = end-start+1
                midpoint = start + (length//2)
                #print(f"s = {start}, e ={end}, m = {midpoint}")

                if target < nums[midpoint]:
                    #print("less")
                    return search(start,midpoint-1,search_for_first)                    
                elif target > nums[midpoint]:
                    #print("greater")
                    return search(midpoint+1,end,search_for_first)      
                else:
                    #print("equal")
                    if search_for_first:
                        ans = search(start,midpoint-1,search_for_first)
                        if ans == -1:
                            ans = midpoint
                    else:
                        ans = search(midpoint+1,end,search_for_first)
                        if ans == -1:
                            ans = midpoint
                    return ans
                
        return [search(0,n-1,True), search(0,n-1,False)]
                    
            
        
        
# Complexity analysis
#O(log |list|)
