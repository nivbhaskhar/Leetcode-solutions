#https://leetcode.com/problems/buildings-with-an-ocean-view/description/
import math
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        if n == 0:
            return []

        ans = []
        max_from_end = -math.inf
        for i in range(n-1,-1,-1):
            if heights[i] > max_from_end:
                ans.append(i)
                max_from_end = heights[i]
        return reversed(ans)
      

    def findBuildingsSort(self, heights: list[int]) -> list[int]:
        indices_and_heights = sorted(list(enumerate(heights)), key=lambda x: x[1], reverse=True)
        blocked_indices = set()
        rightmost_index = -1
        rightmost_height = math.inf
        #print(indices_and_heights)
        for i, ht in indices_and_heights:
            #print(f"i = {i}, ht = {ht}, rightmost_index = {rightmost_index}, rightmost_height = {rightmost_height}")
            if i > rightmost_index:
                if ht == rightmost_height:
                    blocked_indices.update(set(range(rightmost_index,i)))
                elif ht < rightmost_height:
                    blocked_indices.update(set(range(rightmost_index+1,i)))
                #print(blocked_indices)
                rightmost_index = i
                rightmost_height = ht
        return [i for i in range(len(heights)) if i not in blocked_indices]



        