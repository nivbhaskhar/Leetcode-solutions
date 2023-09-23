#https://leetcode.com/problems/find-k-th-smallest-pair-distance/

import heapq

class Solution:

    def num_pairs_with_difference_lowerbound(self, val: int, nums: list[int])->int:
        n = len(nums)
        end = 1
        start = 0
        num_pairs = 0
        while(end < n):
            while(start < end and nums[end]-nums[start]>val):
                start += 1
            num_pairs += end-start
            end += 1
        return num_pairs

    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if n<=1:
            return None
        high = nums[n-1]-nums[0]
        low = -1
        while (low < high):
            if high - low == 1:
                return high
            mid = (high + low)//2
            if self.num_pairs_with_difference_lowerbound(mid, nums)>= k:
                high = mid
            else:
                low = mid
        return high



    def smallestDistancePairInefficient(self, nums: list[int], k: int) -> int:
        nums.sort()
        min_distances = []
        heapq.heapify(min_distances)
        n = len(nums)

        for start in range(n):
            for end in range(start+1, min(n,start+k+1)):
                distance = -abs(nums[end]-nums[start])
                #print(f"start = {start}, end = {end}, distance = {distance}")
                heapq.heappush(min_distances, distance)
                if len(min_distances) > k:
                    heapq.heappop(min_distances)
                #print(f"heap = {min_distances}")

        if len(min_distances) == k:
            return -min_distances[0]
        else:
            return None