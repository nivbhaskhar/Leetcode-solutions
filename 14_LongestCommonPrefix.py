#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_characters =[]
        for characters in zip(*strs):
            for i in range(len(characters)-1):
                if characters[i] != characters[i+1]:
                    return "".join(prefix_characters)
            prefix_characters.append(characters[0])
        return "".join(prefix_characters)
    

    def longestCommonPrefix_v2(self, strs: list[str]) -> str:
        prefix_characters =[]
        n = min(len(str) for str in strs)
        for j in range(n):
            for k in range(len(strs)-1):
                if strs[k][j] != strs[k+1][j]:
                    return "".join(prefix_characters)
            prefix_characters.append(strs[0][j])
        return "".join(prefix_characters)