#https://leetcode.com/problems/best-meeting-point/description/
from collections import defaultdict
import math

class Solution:
    def get_distance(self, candidate: int, positions: dict[int, int])->int:
        distance = 0
        for pos, count in positions.items():
            distance += abs(pos-candidate)*count
        return distance

    def get_optimal_distance(self, candidates: list[int],positions: dict[int, int])->int:
        min_distance = math.inf
        for candidate in candidates:
            candidate_distance = self.get_distance(candidate, positions)
            min_distance = min(min_distance, candidate_distance)
        return min_distance

    def get_median(self, positions: dict[int, int], max_key: int)->int:
        total = sum(positions.values())
        mid_value = math.ceil(total/2)
        cumulative_sum = 0
        for pos in range(max_key):
            cumulative_sum += positions[pos]
            if cumulative_sum >= mid_value:
                return pos
        assert False

    def minTotalDistanceInefficient(self, grid: list[list[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        x_coordinates = defaultdict(int)
        y_coordinates = defaultdict(int)
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    x_coordinates[i] += 1
                    y_coordinates[j] += 1
        
        
        min_x_distance = self.get_optimal_distance(range(num_rows), x_coordinates)
        min_y_distance = self.get_optimal_distance(range(num_cols), y_coordinates)
        return min_x_distance + min_y_distance

    def minTotalDistance(self, grid: list[list[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        x_coordinates = defaultdict(int)
        y_coordinates = defaultdict(int)
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    x_coordinates[i] += 1
                    y_coordinates[j] += 1
        
        
        median_x = self.get_median(x_coordinates, num_rows)
        median_y = self.get_median(y_coordinates, num_cols)
        min_x_distance = self.get_distance(median_x, x_coordinates)
        min_y_distance = self.get_distance(median_y, y_coordinates)
        return min_x_distance + min_y_distance