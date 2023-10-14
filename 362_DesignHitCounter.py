#https://leetcode.com/problems/design-hit-counter/

from collections import deque
class HitCounter:

    def __init__(self):
        self.time_stamps = deque([])
        
    def hit(self, timestamp: int) -> None:
        self.time_stamps.append(timestamp)
        #print(timestamp, self.time_stamps, "hit")

        

    def getHits(self, timestamp: int) -> int:
        while self.time_stamps and self.time_stamps[0] <= timestamp-300:
            self.time_stamps.popleft()
        #print(timestamp, self.time_stamps, "gethits")
        return len(self.time_stamps)

 