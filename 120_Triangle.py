#https://leetcode.com/problems/triangle/

class Solution:
    def checkShape(self, triangle: list[list[int]])->bool:
        num_rows = len(triangle)
        for r in range(num_rows):
            if len(triangle[r]) != r+1:
                return False
        return True

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not self.checkShape(triangle):
            raise AssertionError(f"Not a triangle {triangle}")
        num_rows = len(triangle)
        prev_min_sums = []
        for r in range(num_rows):
            min_sums = [0]*(r+1)
            for c in range(r+1):
                val = triangle[r][c]
                if len(prev_min_sums) == 0:
                    min_sums[c] = val
                else:
                    if c == 0:
                        min_sums[c] = val + prev_min_sums[c]
                    elif c < len(prev_min_sums):
                        min_sums[c] = val + min(prev_min_sums[c-1], prev_min_sums[c])
                    else:
                        min_sums[c] = val + prev_min_sums[c-1]
            #print(r, prev_min_sums, min_sums)
            prev_min_sums = min_sums

        if len(prev_min_sums) == 0:
            return 0
        return min(prev_min_sums)


    def minimumTotalMoreExplicitEdgeCases(self, triangle: list[list[int]]) -> int:
        if not self.checkShape(triangle):
            raise AssertionError(f"Not a triangle {triangle}")
        num_rows = len(triangle)
        if num_rows == 0:
            return 0
        elif num_rows == 1:
            return triangle[0][0]
        else:
            prev_min_sums = [triangle[0][0]]
            for r in range(1,num_rows):
                min_sums = [0]*(r+1)
                for c in range(r+1):
                    val = triangle[r][c]
                    if c == 0:
                        min_sums[c] = val + prev_min_sums[c]
                    elif c < len(prev_min_sums):
                        min_sums[c] = val + min(prev_min_sums[c-1], prev_min_sums[c])
                    else:
                        min_sums[c] = val + prev_min_sums[c-1]
                prev_min_sums = min_sums

            return min(prev_min_sums)





        