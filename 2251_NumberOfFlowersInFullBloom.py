#https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/

import heapq
from collections import deque
class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        flowers.sort(key = lambda bloom_times: bloom_times[0])
        flowers = deque(flowers)
        pos_and_arrival_times = sorted(list(enumerate(people)), key = lambda pos_and_arrival_time: pos_and_arrival_time[1])
        num_flowers_in_bloom = [0]*len(people)
        end_times = []

        for pos, current_time in pos_and_arrival_times:
            while flowers and flowers[0][0] <= current_time:
                bloom_time = flowers.popleft()
                end_time = bloom_time[1]
                if end_time >= current_time:
                    heapq.heappush(end_times, end_time)
            while end_times and end_times[0] < current_time:
                heapq.heappop(end_times)
            num_flowers_in_bloom[pos] = len(end_times)

        return num_flowers_in_bloom




