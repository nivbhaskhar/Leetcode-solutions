#https://leetcode.com/problems/kth-largest-element-in-an-array/
import random
class Solution:
    def find_kth_largest_recursive(self, nums: list[int], k: int, start_pos:int, end_pos: int)->int:
        assert end_pos-start_pos+1>=k, f"invalid {k} for s={start_pos}, e={end_pos}"
        if start_pos == end_pos:
            return nums[start_pos]

        pivot_index = random.randint(start_pos, end_pos)
        pivot_value = nums[pivot_index]

        # move pivot to end pos
        nums[pivot_index] = nums[end_pos]
        nums[end_pos] = pivot_value

        num_pivot_values = 0
        to_do_pointer = start_pos
        separating_pointer = start_pos
        equal_pointer = end_pos-1

        # to_do_pointer = x, have to process nums[x]
        # separating_pointer = x means nums[start_pos]....nums[x-1] (is in < v)

        # equal_pointer = x means nums[equal_pointer+1]...nums[end_pos] is ==v

        #[start_pos, separating_pointer-1] < v
        #[separating_pointer,....,equal_pointer] > v
        #[equal_pointer+1,...end_pos] == v

        # [..<v, >v ,..., =v]

        while to_do_pointer <= equal_pointer:
            current_value = nums[to_do_pointer]
            if current_value < pivot_value:
                nums[separating_pointer],nums[to_do_pointer] = nums[to_do_pointer],nums[separating_pointer]
                separating_pointer += 1
                to_do_pointer += 1
            elif current_value == pivot_value:
                nums[equal_pointer],nums[to_do_pointer] = nums[to_do_pointer],nums[equal_pointer]
                equal_pointer -=1
            else:
                to_do_pointer += 1


            

        #[start_pos, separating_pointer-1] < v
        #[separating_pointer,....,equal_pointer] > v
        #[equal_pointer+1,...end_pos] == v
        num_larger = equal_pointer - separating_pointer + 1 
        num_equal = end_pos - equal_pointer
        num_smaller = separating_pointer-start_pos

        [num_smaller, num_equal, num_larger]
        if num_larger >=k:
            return self.find_kth_largest_recursive(nums, k, separating_pointer, equal_pointer)
        elif num_larger + num_equal >= k:
            return pivot_value
        else:
            return self.find_kth_largest_recursive(nums, k-(num_larger+num_equal), start_pos, separating_pointer-1)
        
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.find_kth_largest_recursive(nums, k, 0, len(nums)-1)
        
        