#https://leetcode.com/problems/insert-delete-getrandom-o1/description/
import random
class RandomizedSet:

    def __init__(self):
        self.values_to_positions = {}
        self.values = []
        

    def insert(self, val: int) -> bool:
        if val in self.values_to_positions:
            return False
        else:
            self.values.append(val)
            self.values_to_positions[val] = len(self.values)-1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.values_to_positions:
            pos = self.values_to_positions[val]
            temp_val = self.values[-1]
            self.values[pos] = temp_val
            self.values.pop()
            self.values_to_positions[temp_val] = pos
            del self.values_to_positions[val]
            return True
        else:
            return False
        
    
    def getRandom(self) -> int:
        pos = random.randrange(0,len(self.values))
        return self.values[pos]