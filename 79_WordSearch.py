#https://leetcode.com/problems/word-search/
class Solution:
    def isValidPos(self, x: int, y: int, m: int, n:int)->bool:
        valid_x = x>=0 and x<m
        valid_y = y>=0 and y<n
        return valid_x and valid_y

    def suffixExists(self, m: int, n: int, board: list[list[str]], word: str, start: tuple[int, int],  suffix_pos: int, visited: Dict[Tuple[int,int], bool])->bool:
        i, j = start
        #print(f"dfs start = i = {i}, j = {j}, suffix_pos = {suffix_pos}")
        if word[suffix_pos] != board[i][j]:
            return False
        visited[(i, j)] = True
        if suffix_pos == len(word)-1:
            return True
        nbhrs = [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]
        for nbhr_x, nbhr_y in nbhrs:
            if self.isValidPos(nbhr_x, nbhr_y, m, n) and not visited[(nbhr_x, nbhr_y)]:
                if self.suffixExists(m, n, board, word, (nbhr_x, nbhr_y), suffix_pos + 1, visited):
                    return True
        # to make backtracking work, we should remember to reset if we cannot continue the solution from (i,j).
        visited[(i, j)] = False
        return False


    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        m = len(board)
        n = len(board[0])
        start_positions = [(i,j) for i in range(m) for j in range(n)]
        for start_x, start_y in start_positions:
            #print(f"start = {start_x}, {start_y}")
            visited = {(i,j): False for i in range(m) for j in range(n)}
            if self.suffixExists(m, n, board, word, (start_x, start_y), 0, visited):
                return True
        return False

        