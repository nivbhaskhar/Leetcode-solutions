#https://leetcode.com/problems/group-shifted-strings/description/
from collections import defaultdict
class Solution:
    def get_numerical_representation(self, string: str) -> list[int]:
        if len(string) == 0:
            raise ValueError(f"empty strings are not allowed")
        elif ord(string[0]) < 97 or ord(string[0]) > 122:
            raise ValueError(f"invalid character {string[0]} at pos {0}")

        rep = []

        for i in range(1,len(string)):
            if ord(string[i]) < 97 or ord(string[i]) > 122:
                raise ValueError(f"invalid character {string[i]} at pos {i}")
            rep.append((ord(string[i])-ord(string[i-1])) % 26)
        
        return rep

    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        numerical_rep_to_strings = defaultdict(list)
        for string in strings:
            numerical_rep = tuple(self.get_numerical_representation(string))
            numerical_rep_to_strings[numerical_rep].append(string)
        
        #print(numerical_rep_to_strings)
        return list(numerical_rep_to_strings.values())