#https://leetcode.com/problems/number-of-good-pairs/


from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        c = Counter(nums)
        num_pairs = 0
        for val in c.values():
            num_pairs += val*(val-1)//2
        return num_pairs

        