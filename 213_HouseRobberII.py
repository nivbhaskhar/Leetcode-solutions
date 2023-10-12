#https://leetcode.com/problems/house-robber-ii/
from typing import Optional
class Solution:
    def get_min_non_nbhr(self, i: int, j: int)->Optional[int]:
        if i+2 <= j:
            return i+2
        else:
            return None
    def get_max_non_nbhr(self, i: int, j: int, n: int)->Optional[int]:
        if i!=0:
            return j
        elif i==0 and j!=n-1:
            return j
        else:
            if j-1>i:
                return j-1
            else:
                return None
    
    def is_valid_window(self, min_non_nbhr:Optional[int], max_non_nbhr: Optional[int])->bool:
        return (min_non_nbhr and max_non_nbhr and (min_non_nbhr <= max_non_nbhr))

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        current_end = 0
        money_for_prev_end = {} # stores {start: max money in nums[start: prev_end+1] for start <= prev_end}
        money_for_current_end = {} # stores {start: max money in nums[start: current_end+1] for start <= current_end}
        while (current_end<n):
            # update money_for_current_end using money_for_prev_end
            for start in range(current_end, -1, -1):
                if start == current_end:
                    money_for_current_end[start] = nums[start]
                else:
                    candidate_max = nums[start]
                    min_non_nbhr = self.get_min_non_nbhr(start, current_end)
                    max_non_nbhr = self.get_max_non_nbhr(start, current_end, n)
                    if self.is_valid_window(min_non_nbhr, max_non_nbhr):
                        assert max_non_nbhr in [current_end, current_end-1], f"invalid {max_non_nbhr} of {start} for {current_end}"
                        if max_non_nbhr == current_end:
                            assert min_non_nbhr > start, f"invalid {min_non_nbhr} of {start} for {current_end} = max_non_nbhr"
                            candidate_max += money_for_current_end[min_non_nbhr]
                        else:
                            candidate_max += money_for_prev_end.get(min_non_nbhr, 0)


                    money_for_current_end[start] = max(money_for_current_end[start+1], candidate_max)

            #print(f"current end = {current_end}")
            #pprint.pprint(money_for_current_end)
            current_end += 1
            money_for_prev_end = money_for_current_end
            money_for_current_end = {}
        
        return money_for_prev_end[0]


        