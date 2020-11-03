#https://leetcode.com/problems/subsets/
import itertools
class Solution:
    def subsets_itertools(self, nums: List[int]) -> List[List[int]]:
        ans_list = []
        for i in range(len(nums)+1):
            for p in itertools.combinations(nums, i):
                ans_list.append(p)
        return(ans_list)

    def subsets_backtrack(self, nums: List[int]) -> List[List[int]]:
         ans_list = []
         subset_so_far = []
        def dfs(pos):
            #print(f"pos is {pos}")
            #print(f"subset is {subset_so_far}")
            if pos == len(nums):
                #print(f"at leaf node subset is {subset_so_far}")
                #add a copy of state if state is changing!
                ans_list.append(subset_so_far[:])
                #print(f"ans_list is {ans_list}")
            else:
                # do not add nums[pos]
                dfs(pos+1)
                # add nums[pos]
                subset_so_far.append(nums[pos])
                dfs(pos+1)
                subset_so_far.pop()
                dfs(0)
                
        return ans_list

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans_list= []
        for i in range(2**n):
            subset = []
            for j in range(n):
                j_bit = (i>>j) & 1
                if j_bit == 1:
                    subset.append(nums[j])
            
            ans_list.append(subset)      
        return ans_list

#Complexity
#O(n*2^n) where n = len(nums)
