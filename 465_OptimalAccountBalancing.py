#https://leetcode.com/problems/optimal-account-balancing/description/

from collections import defaultdict
class Solution:

    def get_net_balance(self, transactions: list[list[int]])->dict[int, int]:
        net_balance = defaultdict(int)
        for transaction in transactions:
            giver = transaction[0]
            receiver = transaction[1]
            amount = transaction[2]
            net_balance[giver] -= amount
            net_balance[receiver] += amount
        return net_balance

    def min_transfers_recursive(self, pos: int, net_balances: List[int])->int:
        self.c += 1
        ans = math.inf
        n = len(net_balances)
        #print(f"c = {self.c}, pos = {pos}, balance = {net_balances}")
        if pos >= n:
            return 0
        elif pos == n-1:
            assert net_balances[pos] == 0, f"something went wrong"
            return 0
        else:
            if net_balances[pos] == 0:
                return self.min_transfers_recursive(pos+1, net_balances)
            else:
                for next_pos in range(pos+1,n):

                    val = net_balances[pos]
                    if val*net_balances[next_pos] < 0:
                        net_balances[next_pos] += val
                        net_balances[pos] = 0
                        temp = self.min_transfers_recursive(pos + 1, net_balances)
                        ans = min(ans, 1+temp)
                        net_balances[next_pos] -= val
                        net_balances[pos] = val
                return ans



    def minTransfers(self, transactions: List[List[int]]) -> int:
        self.c = 0
        net_balance = self.get_net_balance(transactions)
        #print(net_balance)

        people = sorted(net_balance.keys())
        net_balances = [net_balance[person] for person in people]
        #print(net_balances)
        ans = self.min_transfers_recursive(0, net_balances)
        #print(f"final c = {self.c}")
        return ans




     
