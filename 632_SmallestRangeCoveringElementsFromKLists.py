# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import math
from collections import deque
import heapq

class MultiSet:
    def __init__(self):
        self.elements = {}
    
    def add(self, new_elements):
        for x in new_elements:
            if x not in self.elements:
                self.elements[x] = 1
            else:
                self.elements[x] += 1
    
    def remove(self, elements_to_remove):
        for x in elements_to_remove:
            if self.elements[x] == 1:
                del self.elements[x]
            else:
                self.elements[x] -= 1
    
    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)
    
    def __repr__(self):
        return repr(self.elements)

class Solution:
    def get_indicators(self, nums: list[list[int]])->dict[int, set[int]]:
        indicators = defaultdict(set)
        for pos, l in enumerate(nums):
            for elem in l:
                indicators[elem].add(pos)
        #print(f"indicators = {indicators}")
        return indicators

    def merge(self, nums: list[list[int]])->list[int]:
        nums_q = [deque(l) for l in nums]
        min_heap = []
        for i,l in enumerate(nums_q):
            if l:
                elem = l.popleft()
                min_heap.append((elem, i))
        heapq.heapify(min_heap)
        merged = []
        while min_heap:
            elem, list_pos = heapq.heappop(min_heap)
            if len(merged) == 0 or merged[-1] != elem:
                merged.append(elem)
            if nums_q[list_pos]:
                new_elem = nums_q[list_pos].popleft()
                heapq.heappush(min_heap,(new_elem, list_pos))
        #print(f"merged = {merged}")
        return merged
        
    def slidingWindow(self, merged: list[int], indicators: dict[int, set[int]], num_lists: int)->tuple[int, int]:
        #print(merged)
        n = len(merged)
        start = 0
        min_length = math.inf
        ans_window = (merged[0], merged[n-1])
        container_lists = MultiSet()
        for end in range(n):
            container_lists.add(indicators[merged[end]])
            # window under consideration is merged[start:end+1]
            #print(start,end, container_lists)
            while len(container_lists) == num_lists and start<=end:
                #print(f"valid {container_lists}")
                current_length = merged[end]-merged[start]+1
                if current_length < min_length:
                    min_length = current_length
                    ans_window = (merged[start], merged[end])
                container_lists.remove(indicators[merged[start]])
                start += 1
                #print(start,end,"valid_next??")
                #print(f"valid next {container_lists}")

        return ans_window


    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        num_lists = len(nums)
        merged = self.merge(nums)
        indicators = self.get_indicators(nums)
        start, end = self.slidingWindow(merged, indicators, num_lists)
        return [start, end]
        