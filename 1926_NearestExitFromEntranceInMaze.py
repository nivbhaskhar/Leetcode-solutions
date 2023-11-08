#https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

Idea:

bfs from entrance, store level along with vertex in to_explore queue
detect if exit each time you look at unvisited nbhrs of the current vertex