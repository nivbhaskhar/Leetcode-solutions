#https://leetcode.com/problems/as-far-from-land-as-possible/submissions/

import pprint
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def nbhrs(i,j):
            list_of_nbhrs = []
            if j-1 >= 0:
                list_of_nbhrs.append((i,j-1))
            if j+1 < cols:
                list_of_nbhrs.append((i,j+1))
            if i-1 >= 0:
                list_of_nbhrs.append((i-1,j))
            if i+1 < rows:
                 list_of_nbhrs.append((i+1,j))
            return list_of_nbhrs
        
        to_be_explored = deque([])
        distances = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    distances[(i,j)]=0
                    to_be_explored.append((i,j))
        while(to_be_explored):
            i,j = to_be_explored.popleft()
            current_distance = distances[(i,j)]
            list_of_nbhrs = nbhrs(i,j)
            for nbhr in list_of_nbhrs:
                if nbhr not in distances:
                    distances[nbhr] = current_distance + 1
                    to_be_explored.append(nbhr)
        #pprint.pprint(distances)
        max_distance = -1
        for i,j in distances:
            max_distance = max(max_distance, distances[(i,j)])
        if max_distance == 0:
            max_distance = -1
        return max_distance
                    
     

                   

# Complexity analysis
# BFS with a longer starting queue. O(V+E) where V is the number of vertices and E the number of edges. Here V~N^2 where N is len of grid and degree of each vertex ~ 4. So number of edges = 4N^2/2 = 2N^2. So O(N^2)





