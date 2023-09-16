# https://leetcode.com/problems/minimum-number-of-refueling-stops/


import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        # append a dummy station at target with 0 fuel
        stations.append([target, 0]) 


        # tracks answer = min num of refuelling stops
        num_stops = 0

        # tracks prev pos of car
        prev_pos = 0

        # tracks current fuel in tank
        current_fuel = startFuel

        # max heap of stations seen thus far which we can retroactively refuel from
        max_heap = []
        heapq.heapify([])

        for pos, capacity in stations:

            # car has travelled from prev_pos to pos
            prev_distance = pos - prev_pos
            # so car has used up prev_distance amount of fuel
            current_fuel -= prev_distance

            # retroactively try to refuel from largest gas stations in heap till current_fuel is non-negative
            while current_fuel < 0 and max_heap:
                current_fuel += -heapq.heappop(max_heap)
                num_stops += 1

            # if that still doesn't help, we can never reach target
            if current_fuel < 0:
                return -1
            
            # add current station to max heap
            heapq.heappush(max_heap, -capacity)

            # update prev_pos
            prev_pos = pos

        return num_stops
    

# Complexity analysis
# popping max element from max heap --> O(log n) where n is size of heap
# might want to pop all elements from max heap --> O(n log n) where n is size of heap
# note that heap size is at most n, n = num stations at any point
# updating heap --> O(n log n)

# O(n log n)

