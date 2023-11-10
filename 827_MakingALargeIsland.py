#https://leetcode.com/problems/making-a-large-island/description/

class Grid:
    def __init__(self, grid:list[list[int]]):
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
    
    def is_valid(self, cell: tuple[int, int])->bool:
        x, y = cell
        return x>=0 and x<self.num_rows and y>=0 and y<self.num_cols and self.grid[x][y] == 1

    def get_nbhrs(self, cell: tuple[int,int])->list[tuple[int,int]]:
        x, y = cell
        possible_nbhrs = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        return [nbhr for nbhr in possible_nbhrs if self.is_valid(nbhr)]

    def dfs(self, cell: tuple[int,int], visited: dict[tuple[int,int], int], label: int, num_nodes: int)->int:
        visited[cell] = label
        num_nodes += 1
        for nbhr in self.get_nbhrs(cell):
            if visited[nbhr] == -1:
                num_nodes = self.dfs(nbhr, visited, label, num_nodes)
        return num_nodes

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        my_grid = Grid(grid)
        visited = {(i,j): -1 for i in range(my_grid.num_rows) for j in range(my_grid.num_cols) if grid[i][j]==1}
        component_size = {}
        label = 1
        for i in range(my_grid.num_rows):
            for j in range(my_grid.num_cols):
                if grid[i][j]==1 and visited[(i,j)]==-1:
                    num_nodes = my_grid.dfs((i,j), visited, label,0)
                    component_size[label] = num_nodes
                    label += 1

        if len(component_size) == 0:
            max_size = 0
        else:
            max_size = max(component_size.values())


        for i in range(my_grid.num_rows):
            for j in range(my_grid.num_cols):
                if grid[i][j] == 0:
                    nbhrs = my_grid.get_nbhrs((i,j))
                    labels = set(visited[nbhr] for nbhr in nbhrs)
                    new_component = sum([component_size[label] for label in labels])+1
                    if new_component > max_size:
                        max_size = new_component

        return max_size


