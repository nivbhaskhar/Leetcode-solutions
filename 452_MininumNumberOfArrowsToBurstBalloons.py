#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
class Solution:
    def findIntersection(self, current_interval: list[int], next_interval: list[int])->tuple[bool, list[int]]:
        """
        Given two intervals [a,b] and [c,d] with a<=c, returns True, [x,y] if the intervals intersect where [x,y] = intersection
        else returns False, [] if the intervals don't intersect
        """
        current_start = current_interval[0]
        next_start = next_interval[0]
        current_end = current_interval[1]
        next_end = next_interval[1]
        if current_start > next_start:
            raise ValueError(f"except {current_interval} to be earlier interval than {next_interval}")
        if next_start > current_end:
            return False, []
        else:
            intersection_end = min(current_end, next_end)
            return True, [next_start, intersection_end]

    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[0], reverse = True)
        shots = 0
        while len(points) > 0:
            current_interval = points.pop()
            if len(points) == 0:
                shots += 1
            else:
                next_interval = points[-1]
                do_intersect, intersection_interval = self.findIntersection(current_interval, next_interval)
                if do_intersect:
                    points.pop()
                    points.append(intersection_interval)
                else:
                    shots += 1
        return shots