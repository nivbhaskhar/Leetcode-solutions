#https://leetcode.com/problems/champagne-tower/description/
from collections import defaultdict

class Solution:
    def get_parents(self, r: int, c: int)->list[int]:
        possible_parents = [(r-1,c-1), (r-1,c)]
        return [y for (x,y) in possible_parents if x>=0 and y>=0 and y<=x]

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row <0 or query_row >99 or query_glass < 0 or query_glass > query_row:
            raise ValueError(f"invalid query {query_row, query_glass}")

        if query_row == 0:
            return min(1, poured)
        
        prev_overflow = defaultdict(int)
        prev_overflow[0] = max(poured-1,0)
        for r in range(1,query_row):
            curr_overflow = defaultdict(int)
            for c in range(r+1):
                curr_overflow[c] = max(0,sum([prev_overflow[y] for y in self.get_parents(r,c)])/2 - 1)
            prev_overflow = curr_overflow
            #print(r, prev_overflow)
        
        return min(sum([prev_overflow[y] for y in self.get_parents(query_row,query_glass)])/2, 1)