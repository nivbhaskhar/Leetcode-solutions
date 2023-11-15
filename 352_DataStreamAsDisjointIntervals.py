#https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
import math
from typing import Optional
class Node:
    def __init__(self, val: int, next_node: Optional['Node']=None, prev_node: Optional['Node']=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node

# TODO -- change to actual implementation of BST
class BST():
    def __init__(self):
        self.data = set()
    
    def add(self, val:int):
        self.data.add(val)

    def remove(self, val:int):
        self.data.remove(val)
    
    def get_predecessor(self, val:int)->Optional[int]:
        if len(self.data) == 0:
            return None

        ans = -math.inf
        for v in self.data:
            if v <= val and v > ans:
                ans = v

        if ans == - math.inf:
            return None
        else:
            return ans
    
    def get_sorted_vals(self)->list[int]:
        return sorted(list(self.data))

class SummaryRanges:

    def __init__(self):
        self.start_to_end = {}
        self.end_to_start = {}
        self.bst = BST()
        

    def addNum(self, val: int) -> None:

        # check if value is a duplicate
        pred = self.bst.get_predecessor(val)
        if pred is not None:
            if self.start_to_end[pred]>= val:
                return
        
        prev_is_end = val-1 in self.end_to_start
        next_is_start = val+1 in self.start_to_end

        if prev_is_end and next_is_start:
            # merge [....-val-1,  val+1:.....]
            s = self.end_to_start[val-1]
            e = self.start_to_end[val+1]
            del self.start_to_end[val+1]
            del self.end_to_start[val-1]
            self.start_to_end[s] = e
            self.end_to_start[e] = s
            self.bst.remove(val+1)

        elif prev_is_end:
            # make [..., val-1] -> [...., val]
            s = self.end_to_start[val-1]
            del self.end_to_start[val-1]
            self.start_to_end[s] = val
            self.end_to_start[val] = s

        elif next_is_start:
            # make [val+1,....] -> [val, ....]
            e = self.start_to_end[val+1]
            del self.start_to_end[val+1]
            self.start_to_end[val] = e
            self.end_to_start[e] = val
            self.bst.remove(val+1)
            self.bst.add(val)

        else:
            # create new [val]
            self.start_to_end[val] = val
            self.end_to_start[val] = val
            self.bst.add(val)
        

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        for s in self.bst.get_sorted_vals():
            e = self.start_to_end[s]
            intervals.append([s,e])
        return intervals
        
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()