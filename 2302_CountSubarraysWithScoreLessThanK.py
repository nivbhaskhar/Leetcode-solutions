#https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        sum_of_window = 0
        len_of_window = 0
        score_of_window = 0
        start = 0
        end = 0
        n = len(nums)
        count = 0
        for end in range(n):
            # window under consideration is nums[start:end+1]
            sum_of_window += nums[end]
            len_of_window += 1
            score_of_window = (sum_of_window)*(len_of_window)
            while score_of_window >= k:
                len_of_window -= 1
                sum_of_window -= nums[start]
                score_of_window = sum_of_window*(len_of_window)
                start += 1
            #[start, end] valid window => any [start +i, end] is also valid window
            count += (end-start+1)
        return  count