#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

import random

class UnionFind:
    def __init__(self, num_nodes:int):
        self.representatives = {i: i for i in range(num_nodes)}
        self.num_components = num_nodes

    def union(self, node_a: int, node_b: int):
        rep_a = self.find(node_a)
        rep_b = self.find(node_b)
        if random.randint(0,1):
            self.representatives[rep_a] = rep_b
        else:
            self.representatives[rep_b] = rep_a
        if rep_a != rep_b:
            self.num_components -= 1


    def find(self, node: int)->int:
        initial_rep = self.representatives[node]
        if initial_rep == node:
            return initial_rep
        final_rep = self.find(initial_rep)
        self.representatives[node] = final_rep
        return final_rep





class Solution:
    def getAdjacencyDict(self, n: int, edges: list[list[int]])->dict[int, list[int]]:
        adjacency_dict = {i: [] for i in range(n)}
        for edge in edges:
            if len(edge) != 2:
                raise ValueError(f"improper edge {edge} in {edges}")
            adjacency_dict[edge[0]].append(edge[1])
            adjacency_dict[edge[1]].append(edge[0])
        return adjacency_dict

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        components = UnionFind(n)
        for edge in edges:
            components.union(edge[0], edge[1])
        num_components = components.num_components
        #for i in range(n):
        #    components.find(i)
        #return len(set([components.representatives[i] for i in range(n)]))
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


    
        