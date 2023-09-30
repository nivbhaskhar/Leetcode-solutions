#https://leetcode.com/problems/coin-change/

import math
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_coins = [math.inf]*(amount+1)
        min_coins[0] = 0
        for a in range(1,amount+1):
            for coin in coins:
                if coin <= a:
                    min_coins[a] = min(min_coins[a], min_coins[a-coin]+1)
        
        if min_coins[amount] == math.inf:
            return -1
        else:
            return min_coins[amount]
        
#Complexity
#O(|coins|*amount)
