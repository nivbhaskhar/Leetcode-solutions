#https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0]*len(pref)
        prev = 0
        for i in range(len(pref)):
            arr[i] = pref[i]^prev
            prev = pref[i]
        return arr