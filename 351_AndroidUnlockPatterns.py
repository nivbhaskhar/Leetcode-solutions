#https://leetcode.com/problems/android-unlock-patterns/

from itertools import permutations
from collections import defaultdict

class Solution:
    def numberOfPatterns(self, m:int, n:int)->int:
        valid_pattern = []
        return self.numExtendedValidPatterns(valid_pattern, m, n)


    def numExtendedValidPatterns(self, pattern: list[int], m: int, n:int)->int:
        if len(pattern) >= n:
            return 0
        num_extended_patterns = 0
        new_digits = [i for i in range(1,10) if i not in pattern]
        for digit in new_digits:
            pattern.append(digit)
            if self.isValid(pattern):
                if m<= len(pattern) and n>= len(pattern):
                    num_extended_patterns += 1
                num_extended_patterns += self.numExtendedValidPatterns(pattern, m, n)
            pattern.pop()
        return num_extended_patterns

    def extendValidPatternsIterative(self, valid_patterns: list[list[int]])->list[list[int]]:
        extended_patterns = []
        for pattern in valid_patterns:
            new_digits = [i for i in range(1,10) if i not in pattern]
            for digit in new_digits:
                pattern.append(digit)
                if self.isValid(pattern):
                    extended_patterns.append(pattern.copy())
                pattern.pop()
        return extended_patterns
        

    def numberOfPatternsIterative(self, m:int, n:int)->int:
        num_patterns = 0
        valid_patterns = [[]]
        for k in range(1,n+1):
            valid_patterns = self.extendValidPatterns(valid_patterns)
            #print(valid_patterns)
            if k >=m:
                num_patterns += len(valid_patterns)
        return num_patterns



    def numberOfPatternsInitial(self, m: int, n: int) -> int:
        #s = set([])
        ans = 0
        for k in range(m, n+1):
            for pattern in permutations(list(range(1,10)), k):
                if self.isValid(list(pattern)):
                    ans += 1
                    #s.add(pattern)
        #pprint.pprint(s)
        return ans
        
    def isValid(self, pattern: list[int])->bool:
        digits_seen = defaultdict(int)
        k = len(pattern)
        for i, digit in enumerate(pattern):
            digits_seen[digit] += 1
            if i+1 < k:
                next_digit = pattern[i+1]
                s = set([digit, next_digit])
                if s == set([1,3]) or s == set([4,6]) or s == set([7,9]) or s == set([1,7]) or s == set([2,8]) or s == set([3,9]) or s == set([1,9]) or s == set([3,7]):
                    mid_digit = (digit + next_digit)//2
                    if digits_seen[mid_digit] == 0:
                        return False
        return True