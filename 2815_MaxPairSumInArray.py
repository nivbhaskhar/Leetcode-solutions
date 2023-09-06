# https://leetcode.com/problems/max-pair-sum-in-an-array/

from collections import defaultdict
class Solution:
    def maxDigit(self, num: int)->int:
        max_digit = 0
        while num > 0:
            last_digit = num % 10
            num = num//10
            max_digit = max(max_digit, last_digit)
        return max_digit
        # return max([int(x) for x in str(num)])
    
    def maxPairSum(self, cluster: list[int])->int:
        if len(cluster) <= 1:
            return -1
        for i in range(len(cluster)-1):
            if cluster[i]>cluster[i+1]:
                cluster[i], cluster[i+1] = cluster[i+1], cluster[i]
        for i in range(len(cluster)-2):
            if cluster[i]>cluster[i+1]:
                cluster[i], cluster[i+1] = cluster[i+1], cluster[i]
        return cluster[-1]+cluster[-2]
    
            
    
    def maxSum(self, nums: list[int]) -> int:
        cluster_by_max_digit = defaultdict(list)
        for num in nums:
            num = abs(num)
            cluster_by_max_digit[self.maxDigit(num)].append(num)
        return max([self.maxPairSum(cluster_by_max_digit[digit]) for digit in cluster_by_max_digit])
    

# Complexity analysis
# max digit of x : O(log x) 
# cluster by max digit : O(n log x) where n is size of nums and x = max(nums)
# max pair sum for each cluster : O(c) where c is size of cluster
# so overall complexity = O(n log x) + sum O(c) = O(n log x) + O(n) = O(n log x)