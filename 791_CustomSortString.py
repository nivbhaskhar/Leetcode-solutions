#https://leetcode.com/problems/custom-sort-string/description/

from collections import Counter, defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counter = Counter(s)
        ans = []
        for c in order:
            ans.extend([c]*counter[c])
            counter[c] = 0

        for c in counter:
            ans.extend([c]*counter[c])
            
        return ''.join(ans)



    def customSortStringWithSorting(self, order: str, s: str) -> str:
        rank = defaultdict(lambda: -1)
        for i, character in enumerate(order):
            rank[character]=i

        return ''.join(sorted(s, key = lambda x: rank[x]))