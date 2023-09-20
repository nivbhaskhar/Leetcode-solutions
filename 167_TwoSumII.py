#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers)-1
        while (start < len(numbers) and end >= 0 and start < end):
            current_sum = numbers[start] + numbers[end]
            if current_sum == target:
                return [start+1, end+1]
            elif current_sum < target:
                start += 1
            else:
                end -= 1
        return []