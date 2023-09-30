#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

class Solution:
    def getAdjacencyDict(self, n: int, edges: list[list[int]])->dict[int, list[int]]:
        adjacency_dict = {i: [] for i in range(n)}
        for edge in edges:
            if len(edge) != 2:
                raise ValueError(f"improper edge {edge} in {edges}")
            adjacency_dict[edge[0]].append(edge[1])
            adjacency_dict[edge[1]].append(edge[0])
        return adjacency_dict

    def countComponentsUnionFind(self, n: int, edges: list[list[int]]) -> int:
        adjacency_dict = self.getAdjacencyDict(n, edges)
        num_components = 0
        # TODO
    
        return num_components



    def dfs(self, adjacency_dict: dict[int, list[int]], visited: dict[int, bool], start_node: int):
        visited[start_node] = True
        for nbhr in adjacency_dict[start_node]:
            if not visited[nbhr]:
                self.dfs(adjacency_dict, visited, nbhr)
        

    def countComponentsDFS(self, n: int, edges: list[list[int]]) -> int:
        adjacency_dict = self.getAdjacencyDict(n, edges)
        visited = {i: False for i in range(n)}
        num_components = 0
        for node in range(n):
            if not visited[node]:
                num_components += 1
                self.dfs(adjacency_dict, visited, node)
        
        return num_components


    