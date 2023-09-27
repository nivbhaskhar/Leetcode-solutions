#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        assert len(nums2) == n
        assert len(nums1) == m + n
        fill_pos = m+n-1
        nums1_pos = m-1
        nums2_pos = n-1
        while(fill_pos >=0):
            if nums1_pos >=0 and nums2_pos >=0: 
                elem1 = nums1[nums1_pos]
                elem2 = nums2[nums2_pos]
                if elem2 >= elem1:
                    nums1[fill_pos] = elem2
                    nums2_pos -= 1
                else:
                    nums1[fill_pos] = elem1
                    nums1_pos -= 1
            elif nums2_pos >= 0:
                nums1[fill_pos] = nums2[nums2_pos]
                nums2_pos -= 1
            elif nums1_pos >= 0:
                nums1[fill_pos] = nums1[nums1_pos]
                nums1_pos -=1
            fill_pos -= 1
        return nums1

        