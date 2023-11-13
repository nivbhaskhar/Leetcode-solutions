#https://leetcode.com/problems/add-strings/description/

class Solution:
    def get_num_places(self, num:str)->tuple[int,int]:
        temp = num.split(".")
        if len(temp) == 1:
            return len(temp[0]), 0
        else:
            assert len(temp)==2, f"invalid number format {num}"
            return (len(temp[0]), len(temp[1]))
    
    def get_array_rep(self, num: str, total_whole_places:int, total_decimal_places:int)->list[int]:
        whole_part = [0]*total_whole_places
        decimal_part = [0]*total_decimal_places
        temp = num.split(".")

        whole_places_in_num = len(temp[0])

        diff = total_whole_places - whole_places_in_num
        for i, digit in enumerate(temp[0]):
            whole_part[i+diff] = int(digit)

        if len(temp) > 1:
            for i, digit in enumerate(temp[1]):
                decimal_part[i] = int(digit)

        whole_part.extend(decimal_part)
        return whole_part


    def addStrings(self, num1: str, num2: str) -> str:
        num1_places = self.get_num_places(num1)
        num2_places = self.get_num_places(num2)
        whole_places = max(num1_places[0], num2_places[0])
        decimal_places = max(num1_places[1], num2_places[1])

        num1_arr = self.get_array_rep(num1, whole_places, decimal_places)
        num2_arr = self.get_array_rep(num2, whole_places, decimal_places)

        assert len(num1_arr) == len(num2_arr), f"wrong padding {num1_arr}, {num2_arr}"

        #print(num1_arr, num2_arr)
        ans = []
        carry = 0
        for i in range(len(num1_arr)-1,-1,-1):
            d1 = num1_arr[i]
            d2 = num2_arr[i]
            ans.append(str((carry + d1 + d2) % 10))
            if carry + d1 + d2 >= 10:
                carry = 1
            else:
                carry = 0

        if carry != 0:
            ans.append(str(carry))

        if decimal_places > 0:
            new_ans = ans[:decimal_places]
            new_ans.append(".")
            new_ans.extend(ans[decimal_places:])
        else:
            new_ans = ans
        
        return "".join(reversed(new_ans))


