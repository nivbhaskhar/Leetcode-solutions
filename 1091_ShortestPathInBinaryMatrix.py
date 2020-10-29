#https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import defaultdict, deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        adj_dict = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    for x in [i-1,i,i+1]:
                        if 0<= x and x< N:
                            for y in [j-1,j,j+1]:
                                if 0<=y and y < N:
                                    if (x,y) != (i,j) and grid[x][y]==0:
                                        adj_dict[(i,j)].append((x,y))
        
        s = grid[0][0]
        start = (0,0)
        t = grid[N-1][N-1]
        target = (N-1,N-1)
        if s + t == 0:
            visited = {}
            visited[start]=1
            to_be_explored = deque([(start)])
            while to_be_explored:
                current_vertex = to_be_explored.popleft()
                for nbhr in adj_dict[current_vertex]:
                    if nbhr not in visited:
                        visited[nbhr] = visited[current_vertex] + 1
                        to_be_explored.append(nbhr)
            if target in visited:
                return visited[target]
            else:
                return -1
        else:
            return -1
                               

# Complexity analysis
# |V| <= 10^4 , degree(v) <= 8, |E| <= 8*10^4/2 = 4*10^4
# Setting up the graph - O(|V|)
# BFS - O(|V|+|E|)


