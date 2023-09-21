#https://leetcode.com/problems/4sum/description/
from itertools import combinations
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        k = 4
        n = len(nums)
        ans = set()
        if n < 4:
            return []
        for indices in combinations(range(n-2),k-2):
            #print(f"indices = {list(indices)}")
            # compute sum of nums[i] for i in indices
            current_sum = 0
            for i in range(k-2):
                current_sum += nums[indices[i]]
            new_target = target - current_sum

            # find two elements in nums[start:] which sum to new target
            start = indices[k-3]+1
            end = n-1
            while(start < n and end > start):
                #print([nums[x] for x in indices], nums[start], nums[end], list(indices), start, end)
                s = nums[start] + nums[end]
                if s < new_target:
                    start += 1
                elif s > new_target:
                    end -=1
                else:
                    current_ans = list(indices)
                    current_ans.append(start)
                    current_ans.append(end)
                    #print("ans", tuple(nums[x] for x in current_ans))
                    ans.add(tuple(nums[x] for x in current_ans))
                    start += 1
                    
        return [list(x) for x in ans]