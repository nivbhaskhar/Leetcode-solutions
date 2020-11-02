# https://leetcode.com/problems/permutation-sequence/
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def next_perm(sigma):
            prev_number = -math.inf
            breaking_point = None
            for pos in range(-1,-n-1,-1):
                if sigma[pos] < prev_number:
                    breaking_point = n+pos
                    break
                else:
                    prev_number = sigma[pos]
            if breaking_point is None:
                sigma.reverse()
            else:
                val = sigma[breaking_point]
                new_val = -math.inf
                new_pos = None
                for j in range(breaking_point+1,n):
                    if sigma[j]>val:
                        new_val = sigma[j]
                        new_pos = j
                    else:
                        break
                sigma[breaking_point]=new_val
                sigma[new_pos]=val
                mid_point = breaking_point + ((n-1-breaking_point)//2)
                for j in range(breaking_point+1,mid_point+1):
                    temp = sigma[j]
                    sigma[j] = sigma[n+breaking_point-j]
                    sigma[n+breaking_point-j]=temp
        starting_perm = list(range(1,n+1,1))
        for i in range(k-1):
            next_perm(starting_perm)
            
        return ''.join(map(str, starting_perm))

#Complexity
#O(n) for finding next-perm. So O(kn) for approach 1



    def getPermutation_faster(self, n: int, k: int) -> str:
        ans_list = []
        numbers = list(range(1,n+1))
        def find_starting_term(perm_len, k):
            #print(f"perm_len= {perm_len}, k={k}")
            if perm_len == 0:
                #print("perm_len is 0")
                return
            Q = math.factorial(perm_len-1)
            remainder = k % Q
            if remainder == 0:
                starting_index = (k//Q)
                remainder = Q
            else:
                starting_index = (k//Q)+1
            count = 0
            for i in range(n):
                if numbers[i]!= -1:
                    starting_pos = numbers[i]
                    count += 1
                if count == starting_index:
                    numbers[i]=-1
                    ans_list.append(starting_pos)
                    find_starting_term(perm_len-1, remainder)
                    return
                    
                    
        find_starting_term(n, k)
        print(ans_list)
        return ''.join(map(str, ans_list))
            
                    
#Complexity
#O(n) for finding the s-th least number in a list of size n.
#Recursion called n times, so O(n^2)

                    
                
            
            
                
                    
                
                        
                
                    
                
            
            
        
        
