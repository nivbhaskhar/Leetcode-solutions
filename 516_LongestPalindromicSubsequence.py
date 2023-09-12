# https://leetcode.com/problems/longest-palindromic-subsequence/

from collections import defaultdict
# import pprint
import bisect

class Solution:
    def smallestNumberInInterval(self, a: int, b: int, l: list)->int:
        """
        Given an ordered list of numbers l and a<=b where l definitely contains b, returns the smallest integer x in l which is >= a and <= b
        """
        # placeholder : linear scan
        # for x in l:
        #    if x>=a and x<=b:
        #        return x
        pos = bisect.bisect_left(l, a)
        return l[pos]


    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        char_positions = defaultdict(list)

        # debug = {}

        for pos, c in enumerate(s):
            char_positions[c].append(pos)
        prev_max_length = defaultdict(int)

        for end_pos in range(n):
            current_max_length = defaultdict(int)
            for start_pos in range(end_pos+1):
                x = self.smallestNumberInInterval(start_pos, end_pos, char_positions[s[end_pos]])
                # compute current_max_length from prev_max_length
                if x == end_pos:
                    current_max_length[start_pos] = max(1, prev_max_length[start_pos])
                else:
                    current_max_length[start_pos] = max(2+prev_max_length[x+1], prev_max_length[start_pos])
                #debug[start_pos, end_pos] = current_max_length[start_pos]

            # set prev_max_length = current_max_length
            prev_max_length = current_max_length

        #for a,b in debug:
        #    print(s[a:b+1], debug[a,b])

        return current_max_length[0]



# Complexity: O(n^2 log n)
        