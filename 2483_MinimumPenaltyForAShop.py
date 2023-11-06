#https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

from collections import Counter
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        counter = Counter(customers)
        n = len(customers)

        total_no_in_prefix = counter['N']
        total_yes_in_suffix = counter['Y']

        min_penalty = total_no_in_prefix + total_yes_in_suffix
        best_closing_time = n

        for i in range(n-1,-1,-1):
            if customers[i] == 'N':
                total_no_in_prefix -= 1
            elif customers[i] == 'Y':
                total_yes_in_suffix += 1
            current_penalty = total_no_in_prefix + total_yes_in_suffix 
            if current_penalty <= min_penalty:
                best_closing_time = i
                min_penalty = current_penalty
        
        return best_closing_time
