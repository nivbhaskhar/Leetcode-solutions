# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

from itertools import combinations
from collections import defaultdict
class Solution:

    # solution from problem 516
    def longestPalindromeSubseq(self, s: list[str]) -> int:
        n = len(s)
        
        prev_max_length = defaultdict(int)

        for end_pos in range(n):
            current_max_length = defaultdict(int)
            for start_pos in range(end_pos, -1, -1):
                if start_pos == end_pos:
                    current_max_length[start_pos] = 1
                else:
                    if s[start_pos] == s[end_pos]:
                        current_max_length[start_pos] = 2 + prev_max_length[start_pos+1]
                    else:
                        current_max_length[start_pos] = max(prev_max_length[start_pos], current_max_length[start_pos+1])
                #debug[start_pos, end_pos] = current_max_length[start_pos]

            # set prev_max_length = current_max_length
            prev_max_length = current_max_length

        #for a,b in debug:
        #    print(s[a:b+1], debug[a,b])

        return current_max_length[0]



    def maxProduct(self, s: str) -> int:
        n = len(s)
        positions = list(range(n))
        ans = 0
        for i in range(1,n//2 + 1):
            for subseq in combinations(positions, i):
                first = [x for x in subseq]
                temp = set(first)
                second = [x for x in positions if x not in temp]
                first_subseq = [s[x] for x in first]
                second_subseq = [s[x] for x in second]
                first_length = self.longestPalindromeSubseq(first_subseq)
                second_length = self.longestPalindromeSubseq(second_subseq)
                ans = max(ans, first_length*second_length)
        return ans