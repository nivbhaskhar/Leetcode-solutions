#https://leetcode.com/problems/string-compression/description/
from collections import deque
class Solution:
    def insert_char_and_count(self, chars: list[str], char: str, count: int, overwrite_pos:int)->int:
        chars[overwrite_pos] = char
        overwrite_pos += 1
        if count > 1:
            for digit in str(count):
                chars[overwrite_pos] = digit
                overwrite_pos += 1
        return overwrite_pos

    def compress(self, chars: list[str]) -> int:
        n = len(chars)

        if n <= 1:
            return n
        
        prev_char = chars[0]
        count = 1
        
        overwrite_pos = 0

        for pos in range(1,n):
            current_char = chars[pos]
            if current_char == prev_char:
                count +=1
            else:
                overwrite_pos = self.insert_char_and_count(chars, prev_char, count, overwrite_pos)
                prev_char = current_char
                count = 1
        
        # insert the final character and count
        overwrite_pos = self.insert_char_and_count(chars, prev_char, count, overwrite_pos)
        return overwrite_pos




    


    def compress_with_queue(self, chars: List[str]) -> int:
        n = len(chars)
        chars = deque(chars)
        prev_char = None
        count = 1
        for i in range(n):
            current_char = chars.popleft()
            if current_char == prev_char:
                count += 1
            else:
                chars.append(prev_char)
                if count > 1:
                    for digit in str(count):
                        chars.append(digit)
                
                # reset prev_char and count
                prev_char = current_char
                count = 1

        # append the last character and count
        chars.append(prev_char)
        if count > 1:
            for digit in str(count):
                chars.append(digit)
        # pop the extra None
        chars.popleft()
        return len(chars)

    
