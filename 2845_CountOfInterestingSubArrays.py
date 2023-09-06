#https://leetcode.com/problems/count-of-interesting-subarrays/

from collections import defaultdict

class Solution:
    def modEqualsk(self, num: int, modulo: int, k: int)->int:
        if (num % modulo) == k:
            return 1
        else:
            return 0
        
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        nums = [self.modEqualsk(num, modulo, k) for num in nums]
        # Let c[pos] = number of elements == k mod modulo in [:pos+1]

        # Create dictionary storing {count: list of positions l} 
        # where for each pos in l,  c[pos] = count
        count_to_pos = defaultdict(list)
        count = 0
        ans = 0
        count_to_pos[count].append(-1) # c[-1] = 0 since [:-1+1] = empty array
        for pos,num in enumerate(nums):
            # decide how many interesting subarrays of shape [*,pos] exist
            count += num
            count = (count % modulo)
            # c[pos] = count at this point
            # [*, pos] is interesting if c[pos]-c[*-1] = k mod modulo
            # so [*, pos] is interesting c[*-1] = c[pos] - k mod modulo
            x = (count - k) % modulo 
            # x = c[*-1], the number of *s which satisfy this is exactly len(count_to_pos[x])
            ans += len(count_to_pos[x])
            # update the count_to_pos dictionary for current count
            count_to_pos[count].append(pos)

        return ans
            