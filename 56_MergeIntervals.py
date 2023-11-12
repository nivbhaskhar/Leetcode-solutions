56. Merge Intervals

Problem:
https://leetcode.com/problems/merge-intervals/description/

Idea:
sort intervals by start point

put in a queue

while queue not empty:
	if 1 interval in queue:
          pop interval add to ans list

	otherwise 
	  look at first 2 elements in queue:

           - if overlap, pop both and merge and reinsert the merged interval into queue
           - if no overlap, pop first interval and add to ans list

return ans list


O(n log n) --> sorting , n = num intervals
queue processing is O(n), each time you decrease num intervals in queue

