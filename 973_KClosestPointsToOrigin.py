#https://leetcode.com/problems/k-closest-points-to-origin/
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def euclidean_distance_from_origin(P):
            return -1*math.sqrt(P[0]**2 + P[1]**2)
        N = len(points)
        min_heap = [] 
        heapq.heapify(min_heap)
        distances = list(map(euclidean_distance_from_origin, points))
        for pos, point in enumerate(points):
            no_of_points_in_heap = len(min_heap)
            if len(min_heap) < K:
                heapq.heappush(min_heap,(distances[pos], point))
            elif min_heap[0][0] >= distances[pos]:
                 pass
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,(distances[pos], point))
        return list(map(lambda x: x[1], min_heap))

# Complexity analysis
# Computing distances  -> O(N)
# Size of heap <= K
# Each insertion into heap -> O(log K)
# At most N insertions -> O(N log K)
# So overall O(N log K)

#Cleaner with max-heap but because python has inbuilt min-heap, modified distances to be negative-distances


