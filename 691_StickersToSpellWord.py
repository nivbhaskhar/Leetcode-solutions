#https://leetcode.com/problems/stickers-to-spell-word/description/
from collections import Counter
import math
class Solution:
    def get_candidate_stickers(self, sticker_counters: dict[int, dict], character: str)->list[int]:
        return [i for i in sticker_counters if sticker_counters[i][character] > 0]
    
    def is_contained(self, sticker_1: dict[str, int], sticker_2: dict[str, int])->bool:
        for c in sticker_1:
            if sticker_2.get(c,0) < sticker_1[c]:
                return False
        return True

    def prune_stickers(self, sticker_counters: dict[int, dict], target: str)->list[int]:
        # find sticker positions where target has no overlap with sticker
        irrelevant_sticker_positions = set()
        for i in sticker_counters:
            if sum([sticker_counters[i][character] for character in target]) == 0:
                irrelevant_sticker_positions.add(i)
        
        for i in sticker_counters:
            for j in sticker_counters:
                if i!=j and self.is_contained(sticker_counters[i], sticker_counters[j]):
                    irrelevant_sticker_positions.add(i)

        return list(irrelevant_sticker_positions)

    def get_covered_target(self, sticker_counter: dict[str, int], target_counter: dict[str, int])->dict[str,int]:
        """Give a dictionary of target_letters: count that can be gotten from the sticker"""
        covered_target = {}
        for character in target_counter:
            if character in sticker_counter:
                covered_target[character] = min(target_counter[character], sticker_counter[character])

        return covered_target

    def min_stickers_with_pruning(self, target_counter: dict[str, int], num_targets: int, sticker_counters: dict[int, dict], num_moves_made: int, best_num_moves: int)->int:
        """
        num_targets = sum of values of target_counter
        target_counter describes the letters (with counts) that are yet to be filled
        sticker_counters = coutner of each sticker
        num_moves_made = number of stickers used thus far (imagine you are traversing a tree where root<-> entire target needs to be filled and leaf nodes <--> all target characters filled)
        to reach a node, you would have had to use some number of stickers --> that is num_moves_made

        this is useful for pruning, because if during the traversal, at a node you realize that num_moves_made already exceeds the best_num_moves of a previous path to a leaf, then you don't need to continue on current path [prune it]

        best_num_moves = maintains the best ans as you do dfs style exploration. 
        """

        # At a leaf node
        if num_targets == 0:
            best_num_moves = min(num_moves_made, best_num_moves)
            return best_num_moves

        # prune/stop exploration
        if num_moves_made >= best_num_moves:
            return best_num_moves 

        # pick a letter to fill
        character = ""
        for c in target_counter:
            character = c
            if target_counter[c] > 0:
                break
        
        # try ways to fill this character
        for i in self.get_candidate_stickers(sticker_counters, character):
            covered_target = self.get_covered_target(sticker_counters[i], target_counter)
            num_covered_targets = sum(covered_target.values())

            for character, count in covered_target.items():
                target_counter[character] -= count

            best_num_moves = self.min_stickers_with_pruning(target_counter, num_targets-num_covered_targets, sticker_counters, num_moves_made+1, best_num_moves)

            # backtrack
            for character, count in covered_target.items():
                target_counter[character] += count

        return best_num_moves

    def min_stickers_rec(self, target_counter: dict[str, int], num_targets: int, sticker_counters: dict[int, dict])->int:
        if num_targets == 0:
            return 0
        character = ""
        for c in target_counter:
            character = c
            if target_counter[c] > 0:
                break
        


        
        num_moves = math.inf
        for i in self.get_candidate_stickers(sticker_counters, character):

            covered_target = self.get_covered_target(sticker_counters[i], target_counter)
            num_covered_targets = sum(covered_target.values())

            for character, count in covered_target.items():
                target_counter[character] -= count

            num_moves = min(num_moves, self.min_stickers_rec(target_counter, num_targets-num_covered_targets, sticker_counters))

            for character, count in covered_target.items():
                target_counter[character] += count
        
        return num_moves + 1
        


        
    def minStickers(self, stickers: list[str], target: str) -> int:
        sticker_counters = {i: Counter(stickers[i]) for i in range(len(stickers))}
        target_counter = Counter(target)
        irrelevant_sticker_positions = self.prune_stickers(sticker_counters, target)
        for i in irrelevant_sticker_positions:
            del sticker_counters[i]

        #print(list(sticker_counters.keys()))
        # check if target is achievable
        if not set(target).issubset(set(''.join(stickers))):
            return -1
        #return self.min_stickers_rec(target_counter, len(target),sticker_counters)
        return self.min_stickers_with_pruning(target_counter, len(target),sticker_counters, 0, math.inf)
        






        