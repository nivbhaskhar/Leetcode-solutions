#https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description/
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        A = set(nums1)
        B = set(nums2)
        AB = A.intersection(B)
        a = len(A)
        b = len(B)
        ab = len(AB)

        #add as many unique elements from A not in intersection A\cap B
        x = min(n//2, a-ab) 

        #add as many unique elements from B not in intersection A\cap B
        y = min(n//2, b-ab)

        # add as many elements we can add from A\cap B
        z = min(ab , max(n//2-x, 0) + max(n//2-y,0))
        return x+y+z
        
        ## earlier solution
        # if a<= n//2 and b<= n//2:
        #     return a+b-ab
        # elif a<=n/2 or b<=n/2:
        #     m = min(a,b)
        #     M = max(a,b)
        #     return m + min(n//2, M-ab)
        # else:
        #     x = min(n//2, a-ab)
        #     y = min(n//2, b-ab)
        #     z = 0
        #     if n//2 > x:
        #         z = min(n//2-x, ab)
        #     w = 0
        #     if n//2 > y and ab > z:
        #         w = min(n//2-y, ab-z)
        #     return x+y+z+w
        
        # second attempt: last case generalizes
        # x = min(n//2, a-ab)
        # y = min(n//2, b-ab)
        # z = 0
        # if n//2 > x:
        #     z = min(n//2-x, ab)
        # w = 0
        # if n//2 > y and ab > z:
        #     w = min(n//2-y, ab-z)
        # return x+y+z+w


        