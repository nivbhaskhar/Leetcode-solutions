#https://leetcode.com/problems/house-robber-ii/
from typing import Optional
class Solution:
    def rob_linear(self, nums: list[int])->int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            prev_prev_sum = 0 # f(0) = max for nums[:0]
            prev_sum = nums[0] # f(1) = max for nums[:1]
            for i in range(2, len(nums)+1):
                # compute f(i) = max for nums[:i] = nums[0,1,...i-1]
                new_sum = max(prev_prev_sum + nums[i-1], prev_sum) # f(i)
                prev_prev_sum = prev_sum # update f(i-2) = f(i-1)
                prev_sum = new_sum # update f(i-1) = f(i)
            return prev_sum




    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.rob_linear(nums[:-1]),self.rob_linear(nums[1:]))

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

    def rob_inefficient(self, nums: list[int]) -> int:
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


        