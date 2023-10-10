#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1 
        start = 0
        end = n-1
        while(start < end-1):
            mid = (start + end)//2

            if nums[start] < nums[mid]:
                # [start, mid] --> monotonic inc
                if target >= nums[mid] or target < nums[start]:
                    start = mid
                else:
                    end = mid
  
                
            else:
                # [start, mid] --> monotonic inc and then cliff and then monotonic inc
                if target >= nums[start] or target <= nums[mid]:
                    end = mid
                else:
                    start = mid

        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        else:
            return -1




        # a....b, if a<b --> monotonic
        # a....b.  if a>b --> go up and reach cliff and start from down
        # if a < b, and target between a and b, search in [a,b]
        # if a > b,  a^^^....^^b
        # target > a -> search in [a,b]
        # target < b --> search in
        
    def old_search(self, nums: list[int], target: int) -> int:
        def rec_search(start,end):
            #print(f"s= {start}, e = {end}")
            if start > end:
                return -1
            elif start==end:
                if nums[start]==target:
                    return start
                else:
                    return -1
            elif end==start+1:
                if nums[start]==target:
                    return start
                elif nums[end]==target:
                    return end
                else:
                    return -1
            else:
                length = end-start+1
                (a,c) = (start,start-1+(length//2))
                (b,d) = (start+(length//2),end)
                #print(f"1= ({a},{c}), 2 = ({b},{d})")

                if nums[a] <= nums[c]:
                    if nums[a]<=target and target<=nums[c]:
                        return rec_search(a,c)
                    else:
                        return rec_search(b,d)
                else:
                    if nums[b]<=target and target<=nums[d]:
                        return rec_search(b,d)
                    else:
                        return rec_search(a,c)
            
        return rec_search(0, len(nums)-1)         
                
        
            
        
        
# Complexity analysis
#O(log |list|)
