#https://leetcode.com/problems/rank-transform-of-an-array/description/

import math
class Solution:

    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_pos_and_arr = sorted(enumerate(arr), key = lambda x: (x[1],x[0]))
        ranks = [0]*len(arr)
        prev_val = -math.inf
        rank = 0
        for original_pos, val in sorted_pos_and_arr:
            if val > prev_val:
                rank += 1
            ranks[original_pos] = rank
            prev_val = val
        return ranks
        

