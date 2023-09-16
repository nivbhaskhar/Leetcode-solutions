#https://leetcode.com/problems/jump-game-iii/


from collections import deque
class Solution:
    def dfs(self, start: int, visited: list[bool], arr:int, n: int):
        visited[start] = True
        jump_length = arr[start]
        for sign in [1,-1]:
            nbhr = start+ (sign*arr[start])
            if nbhr < n and nbhr >= 0:
                if not visited[nbhr]:
                    self.dfs(nbhr, visited, arr, n)
  
    def canReachBFS(self, arr: list[int], start: int)-> bool:
        n = len(arr)
        visited = [False]*n
        visited[start] = True
        to_explore = deque([start])
        while len(to_explore) > 0:
            v = to_explore.popleft()
            for sign in [1,-1]:
                nbhr = v + (sign*arr[v])
                if nbhr < n and nbhr >= 0:
                    if not visited[nbhr]:
                        visited[nbhr] = True
                        to_explore.append(nbhr)
        
        reachable_end_nodes = [x for x in range(n) if arr[x] == 0 and visited[x]]
        return len(reachable_end_nodes) > 0 

    def canReachDFS(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        visited = [False]*n
        self.dfs(start, visited, arr, n)
        reachable_end_nodes = [x for x in range(n) if arr[x] == 0 and visited[x]]
        return len(reachable_end_nodes) > 0 