#https://leetcode.com/problems/coin-change-2/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """Computes the number of combinations that make up "amount" using denonimations in "coins" given that there are infinite number of each kind of coin.
        """
       
        coins.sort()
        n = len(coins)
        memo_dict = {}
        #f(i,x) = no_of_ways to make x with coins[i:]
        #want f(0,amount)
        
        def f(start_index,left_over_amount):
            if (start_index, left_over_amount) in memo_dict:
                return memo_dict[(start_index, left_over_amount)]
            
            if start_index >= n and left_over_amount != 0:
                memo_dict[(start_index, left_over_amount)] = 0
                return 0
            elif left_over_amount == 0:
                memo_dict[(start_index, left_over_amount)] = 1
                return 1
            elif left_over_amount < 0:
                memo_dict[(start_index, left_over_amount)] = 0
                return 0
            else:
                memo_dict[(start_index, left_over_amount)] = f(start_index, left_over_amount - coins[start_index]) + f(start_index+1, left_over_amount)
                return memo_dict[(start_index, left_over_amount)]
            

        return f(0,amount)

#Complexity analysis
#0 <= start_index <= len(coins)
#0 <= left_over_amount <= amount
#So need to compute |len(coins)|*amount key value pairs in memo_dict
# Time complexity  - O(len(coins)*amount)
# Space complexity - O(len(coins)*amount)



            
