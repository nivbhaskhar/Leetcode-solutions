#https://leetcode.com/problems/queue-reconstruction-by-height/
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """ Each person in a queue is idenitified by label [h,k] 
        where h is their height and k is the number of people with height >= h.
        Given a list of labels, this recreates the queue
        """
        people.sort(key = lambda x: (-1*x[0], x[1]))
        answerlist = []
        
        for pos,x in enumerate(people):
            answerlist.append((x[0], x[1]))
            height = x[0]
            insert_pos = x[1]
            temp = answerlist[insert_pos]
            for i in range(pos-1,insert_pos-1,-1):
                answerlist[i+1] = answerlist[i]
                
            answerlist[insert_pos] = [height, insert_pos]
            #print(x, answerlist)
            
        return answerlist
                
        
# Complexity analysis 
#n = length of queue
# O(n log n) + O(n^2) = O(n^2)
