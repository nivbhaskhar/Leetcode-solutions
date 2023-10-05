#https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from collections import deque
class Solution:
    def get_nbhrs(self, vertex: tuple[int,int,int], grid: list[list[int]], m: int, n: int, k: int)-> list[tuple[int,int,int]]:
        x, y, obstacles_left = vertex
        planar_nbhrs = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        planar_nbhrs = [(i,j) for (i,j) in planar_nbhrs if 0<=i and i<m and 0<=j and j<n]
        nbhrs = []
        for (i,j) in planar_nbhrs:
            if grid[i][j] == 0:
                nbhrs.append((i,j,obstacles_left))
            if grid[i][j] == 1 and obstacles_left > 0:
                nbhrs.append((i,j,obstacles_left-1))
        return nbhrs


    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = {(p, q, r): False for p in range(m) for q in range(n) for r in range(k+1)}
        to_explore = deque([(0,0,k,0)])
        visited[(0,0,k)] = True
        if m==1 and n==1:
            return 0
        while to_explore:
            current_x, current_y, obstacles_left, current_steps = to_explore.popleft()
            current_vertex = (current_x, current_y, obstacles_left)
            for nbhr in self.get_nbhrs(current_vertex, grid, m, n, k):
                if not visited[nbhr]:
                    x, y, num_obstacles = nbhr
                    if x == m-1 and y == n-1:
                        return current_steps + 1
                    visited[nbhr] = True
                    to_explore.append((x,y,num_obstacles, current_steps+1))
        
        return -1
            


        