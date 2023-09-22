#https://leetcode.com/problems/count-and-say/
class Solution:
    def sayNum(self, digits_of_num: list[str])->list[str]:
        #print(f"start of say num =  {digits_of_num}")
        if len(digits_of_num) <= 0:
            return digits_of_num
    
        ans = []
        prev_digit = None
        count = 0
        for digit in digits_of_num:
            if digit == prev_digit:
                count += 1
            else:
                if prev_digit:
                    ans.append(str(count))
                    ans.append(prev_digit)
                prev_digit = digit
                count = 1
        
        ans.append(str(count))
        ans.append(prev_digit)
        #print(f"end of say num =  {ans}")

        return ans

    def countAndSay(self, n: int) -> str:

        digits_of_num = ['1']

        if n > 1:
            i = 2
            while(i<=n):
                #print(f"i = {i}")
                digits_of_num = self.sayNum(digits_of_num)
                i += 1
            
        return ''.join(digits_of_num)


        