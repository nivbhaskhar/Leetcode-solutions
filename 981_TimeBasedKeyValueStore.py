#https://leetcode.com/problems/time-based-key-value-store/description/

from collections import defaultdict

class TimeMap:

    def __init__(self):
        # key = key, value = [(timestamp_1, value_1), (timestamp_2, value_2)..]
        self.store = defaultdict(lambda :[(-1, "")]) 
        
    def get_value(self, key: str, pos: int)->str:
        return self.store[key][pos][1]

    def get_timestamp(self, key: str, pos:int)->int:
        return self.store[key][pos][0]


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.store[key])
        start = 0
        end = n-1

        if self.get_timestamp(key, end) <= timestamp:
            return self.get_value(key, end)

        while(start < end-1):
            mid = (start + end)//2
            if self.get_timestamp(key, mid) <= timestamp:
                start = mid
            else:
                end = mid
        
        return self.get_value(key, start)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)