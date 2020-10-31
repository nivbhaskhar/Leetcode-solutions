#https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
