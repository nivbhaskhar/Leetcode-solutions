#https://leetcode.com/problems/moving-average-from-data-stream/
import heapq
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.window_length = size
        self.current_sum = 0
        self.values = deque([])
        

    def next(self, val: int) -> float:
        if len(self.values) < self.window_length:
            self.current_sum += val
        else:
            old_val = self.values.popleft()
            self.current_sum += (val - old_val)
        
        self.values.append(val)
        return self.current_sum/len(self.values)


    def __heapinit__(self, size: int):
        self.timestamp = 0
        self.window_length = size
        self.current_sum = 0
        self.timestamps_and_values = []
        heapq.heapify(self.timestamps_and_values)
        

    def heap_next(self, val: int) -> float:
        self.timestamp += 1
        if len(self.timestamps_and_values) < self.window_length:
            self.current_sum += val
            heapq.heappush(self.timestamps_and_values, (self.timestamp, val))
        else:
            old_timestamp, old_val = heapq.heappushpop(self.timestamps_and_values, (self.timestamp,val))
            self.current_sum += (val - old_val)
        return self.current_sum/len(self.timestamps_and_values)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)