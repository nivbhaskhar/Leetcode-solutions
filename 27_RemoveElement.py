#https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        prev_empty_pos = None
        current_pos = 0
        n = len(nums)
        num_other_vals = 0
        while current_pos < n:
            if nums[current_pos] == val:
                nums[current_pos] = None
                if prev_empty_pos is None:
                    prev_empty_pos = current_pos
            else:
                num_other_vals += 1
                if prev_empty_pos is not None:
                    nums[prev_empty_pos] = nums[current_pos]
                    prev_empty_pos += 1
            current_pos += 1
        return num_other_vals
        
        