#https://leetcode.com/problems/maximum-number-of-alloys/description/
import numpy as np
class Solution:
    def within_budget(self, num_alloys: int, budget: int, composition: list[list[int]], stock: list[int], cost: list[int])->bool:
        """
        Given a candidate number of alloys = num_alloys, outputs True if there is any machine which can make it
        from the given stock pile and staying within budget.
        The total cost for manufacturing num_alloys is computed for each machine simultaneously using numpy tricks
        and then we check if there's a machine in it whose total cost <= budget
        """
        new_material_required = np.maximum(num_alloys*np.array(composition)-np.array(stock),0)
        total_cost = np.matmul(new_material_required,np.transpose(np.array([cost])))
        is_within_budget = total_cost <= budget
        return is_within_budget.any(axis=0)[0]

    def maxNumberOfAlloys(self, budget: int, composition: list[list[int]], stock: list[int], cost: list[int]) -> int:
        # In this problem  we implicitly use the fact that cost = function(num alloys) is monotonic increasing

        # find the first num alloys (high) whose total cost to manufacture which exceeds budget
        # by searching powers of 2
        high = 1
        while self.within_budget(high, budget, composition, stock, cost):
                high *= 2
        
        # sets low num alloys to be half of high, whose manufacturing we know is within budget
        low = high//2

        # binary search to find max num alloys whose manufacturing stays within budget
        # low will always be within budget and high above budget
        while(low < high):
            if high-low == 1:
                return low
            mid = (low+high)//2
            if self.within_budget(mid, budget, composition, stock, cost):
                low = mid
            else:
                high = mid
        return low

        