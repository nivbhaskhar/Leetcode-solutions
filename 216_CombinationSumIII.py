#https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def get_valid_combination(self, k: int, n:int, max_num_to_use: int, state: list[int], all_combinations: list[list[int]]):
        if n<= 0:
            return
        elif k == 1:
            if n <= max_num_to_use:
                state.append(n)
                all_combinations.append(state.copy())
                state.pop()
            return
        else:
            for val in range(max_num_to_use, 0, -1):
                state.append(val)
                self.get_valid_combination(k-1, n-val, val-1, state, all_combinations)
                state.pop()
            return





    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        all_combinations = []
        self.get_valid_combination(k, n, 9, [], all_combinations)
        return all_combinations