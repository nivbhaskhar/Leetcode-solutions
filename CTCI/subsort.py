#subsort

import math
def find_slice(nums):
    N = len(nums)
    prev_val = -math.inf
    breaking_point = None
    for pos, val in enumerate(nums):
        if val < prev_val:
            breaking_point = pos
            break
        else:
            prev_val = val


    if breaking_point is None:
        return (None,None)
    else:
        current_min = min(nums[breaking_point:])
        for pos in range(breaking_point):
            if current_min < nums[pos]:
                m = pos
                break


    prev_val = math.inf
    breaking_point = None
    for pos in range(1,N+1):
        val = nums[-pos]
        if val > prev_val:
            breaking_point = pos
            break
        else:
            prev_val = val


    if breaking_point is None:
        return (None,None)
    else:
        current_max = max(nums[:N-pos+1])
        print(f"current_max is {current_max}")
        for pos in range(1,breaking_point):
            if current_max > nums[-pos]:
                n = N-pos
                break

    return (m,n)





print(find_slice([1,2,4,7,10,11,7,12,-1,6,7,16,18,19]))
        
            
        
    
