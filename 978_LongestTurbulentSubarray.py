#https://leetcode.com/problems/longest-turbulent-subarray/


class Solution:
    def maxTurbulenceSize(self, A: list[int]) -> int:
        n = len(A)
        if n==1:
            return 1
        
        
        start = 0
        prev_trend = None
        max_window_length = 0
        
        for end in range(1,n):    
            if A[end]>A[end-1]:
                current_trend = 'inc'
     
            elif A[end]<A[end-1]:
                current_trend = 'dec'
            else:
                current_trend = None
                
            if current_trend and (prev_trend == current_trend):
                start = end - 1
            elif current_trend is None:
                start = end    
                
            max_window_length = max(max_window_length,end-start+1)
            prev_trend = current_trend
            
        return max_window_length        
                   

# Complexity analysis
# Sliding window, O(N) where N is length of A


