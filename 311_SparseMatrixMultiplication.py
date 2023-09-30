#https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def getRowRep(self, mat: list[list[int]])->dict[int, dict[int, int]]:
        """
        Given matrix, output {row: {col: value} representation}
        """
        row_rep = {}
        for r, row in enumerate(mat):
            row_rep[r] = {}
            for c, val in enumerate(row):
                if val:
                    row_rep[r][c] = val
        return row_rep

    def getColRep(self, mat: list[list[int]])->dict[int, dict[int, int]]:
        """
        Given matrix, output {col: {row: value} representation}
        """
        col_rep = {c: {} for c in range(len(mat[0]))}
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                if val:
                    col_rep[c][r] = val
        return col_rep



    def getDotProduct(self, row: dict[int, int], col: dict[int, int])->int:
        dot_product = 0
        for k in row:
            if k in col:
                dot_product += row[k]*col[k]
        return dot_product


    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        mat1_rep = self.getRowRep(mat1)
        mat2_rep = self.getColRep(mat2)
        rows = len(mat1)
        cols = len(mat2[0])
        ans = [[0]*cols for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                ans[r][c] = self.getDotProduct(mat1_rep[r], mat2_rep[c])
        return ans
        