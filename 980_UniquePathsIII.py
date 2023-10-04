#https://leetcode.com/problems/unique-paths-iii/description/

class Graph:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.start = None
        self.end = None
        self.num_vertices = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    if self.start is not None:
                        raise ValueError(f"more than 1 start node")
                    self.start = (i,j)
                    self.num_vertices += 1
                elif grid[i][j] == 2:
                    if self.end is not None:
                        raise ValueError(f"more than 1 end node")
                    self.end = (i,j)
                    self.num_vertices += 1
                elif grid[i][j] == 0:
                    self.num_vertices += 1

    def is_valid_node(self, node: tuple[int, int])->bool:
        i, j = node
        return 0<=i and i<self.m and 0<=j and j<self.n and self.grid[i][j] != -1
    
    def get_nbhrs(self, node: tuple[int,int])->list[tuple[int, int]]:
        i, j = node
        possible_nbhrs = [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]
        return [(x,y) for (x,y) in possible_nbhrs if self.is_valid_node((x,y))]


class Solution:

    def num_hamiltonian_paths(self, current_node: tuple[int,int], visited: set[int], graph: Graph)->int:
        if current_node in visited:
            raise ValueError(f"Something went wrong with recursion, current_node {current_node} is already visited")
        visited.add(current_node)
        if len(visited) == graph.num_vertices and current_node == graph.end:
            num_paths = 1
        elif len(visited) == graph.num_vertices and current_node != graph.end:
            num_paths = 0
        else:
            num_paths = 0
            nbhrs = graph.get_nbhrs(current_node)
            for nbhr in nbhrs:
                if nbhr not in visited:
                    num_paths += self.num_hamiltonian_paths(nbhr, visited, graph)
        visited.remove(current_node)
        return num_paths

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        graph = Graph(grid)
        if graph.start is None or graph.end is None:
            raise ValueError(f"start or end nodes unspecified")
        return self.num_hamiltonian_paths(graph.start, set([]), graph)
        


        


