#https://leetcode.com/problems/find-the-winner-of-an-array-game/description/
class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        assert k>=1, f"invalid k = {k}"
        n = len(arr)
        M = max(arr)
        if k >= n:
            return M

        current_max = max(arr[:k])

        if arr[0] == current_max and arr[0]>arr[k]:
            return arr[0]

        for i in range(k, n):
            current_max = max(current_max, arr[i])
            candidate_pos = i-k+1
            #print(arr[i-k+1], current_max, arr[:i+1])
            if arr[candidate_pos] == current_max:
                return arr[candidate_pos]
        
        return M

        