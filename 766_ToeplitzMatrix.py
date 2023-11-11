#https://leetcode.com/problems/toeplitz-matrix/description/


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])
    
    def next_diagonally(self, cell: Tuple[int,int])->Optional[Tuple[int,int]]:
        x,y = cell
        if 0<= x+1 and x+1< self.num_rows:
            if 0<= y+1 and y+1<self.num_cols:
                return (x+1,y+1)
        return None
    
    def get_top_edge_cells(self)->List[Tuple[int,int]]:
        edge_cells = [(i,0) for i in range(self.num_rows-1,-1,-1)]
        edge_cells.extend([(0,i) for i in range(1,self.num_cols)])
        return edge_cells

    def is_constant_diagonal(self, cell: Tuple[int,int])->bool:
        x,y = cell
        val = self.matrix[x][y]
        while self.next_diagonally(cell):
            cell = self.next_diagonally(cell)
            x, y = cell
            if self.matrix[x][y] != val:
                return False
        return True

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return True
        m = Matrix(matrix)
        edge_cells = m.get_top_edge_cells()
        for edge_cell in edge_cells:
            if not m.is_constant_diagonal(edge_cell):
                return False

        return True