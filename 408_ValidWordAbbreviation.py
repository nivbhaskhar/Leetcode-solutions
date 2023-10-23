#https://leetcode.com/problems/valid-word-abbreviation/description/
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)
        digits = set([str(i) for i in range(10)])
        word_pos = 0
        abbr_pos = 0
        current_digits = []
        while abbr_pos < m and word_pos < n:
            while abbr_pos < m and abbr[abbr_pos] in digits:
                current_digits.append(abbr[abbr_pos])
                abbr_pos += 1
            num_letters_to_skip = ''.join(current_digits)
            current_digits = []
            if num_letters_to_skip:
                if num_letters_to_skip[0]=="0":
                    return False
                    #raise ValueError(f"invalid abbreviation with a leading 0 part {abbr}")
                word_pos += int(num_letters_to_skip)
            if abbr_pos < m and word_pos < n:
                if word[word_pos] != abbr[abbr_pos]:
                    return False
                else:
                    abbr_pos +=1
                    word_pos +=1 
            elif abbr_pos == m and word_pos == n:
                return True
            else:
                return False
        return (word_pos == n and abbr_pos == m)