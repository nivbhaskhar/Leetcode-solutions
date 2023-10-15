#https://leetcode.com/problems/longest-consecutive-sequence

from collections import deque

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_length = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                # num is start of candidate subseq
                current = num
                candidate_subseq_length = 1
                while(current+1 in nums):
                    candidate_subseq_length +=1
                    current += 1
                max_length = max(max_length, candidate_subseq_length)
        return max_length




    def bfs(self, adjacency_dict: dict[int, list[int]], visited: dict[int, int], label: int, start: int)->tuple[int, int]:
        """
        Does BFS from start and returns min and max nodes in connected component
        """
        visited[start] = label
        to_explore = deque([start])
        min_node = start
        max_node = start
        while to_explore:
            current = to_explore.popleft()
            for nbhr in adjacency_dict[current]:
                if visited[nbhr] == 0:
                    visited[nbhr] = label
                    min_node = min(min_node, nbhr)
                    max_node = max(max_node, nbhr)
                    to_explore.append(nbhr)
        return min_node, max_node






    def longestConsecutiveComplicated(self, nums: list[int]) -> int:
        nums = list(set(nums))
        end_to_start = {}
        for num in nums:
            if num in end_to_start:
                continue
            elif num-1 in end_to_start:
                val = end_to_start[num-1]
                del end_to_start[num-1]
                end_to_start[num] = val
            else:
                end_to_start[num] = num
        

        start_to_end = {end_to_start[end]:end for end in end_to_start}

        adjacency_dict = {start:[] for start in start_to_end}
        for start in start_to_end:
            end = start_to_end[start]
            if end+1 in start_to_end:
                adjacency_dict[start].append(end+1)
                adjacency_dict[end+1].append(start)
        
        visited = {start:0 for start in start_to_end}
        label = 1
        max_seq_length = 0
        for start in start_to_end:
            if visited[start] == 0:
                min_node, max_node = self.bfs(adjacency_dict, visited, label, start)
                max_seq_length = max(max_seq_length, start_to_end[max_node]-min_node+1)


            label += 1

        return max_seq_length









        