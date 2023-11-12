270. Closest Binary Search Tree Value

Problem:
https://leetcode.com/problems/closest-binary-search-tree-value/description/

Idea:
do recursion

function (node, target) --> returns val closest to target at subtree rooted at node


v = node.val

if target >= v:
  --> look at candidates = (v, recursive ans on node.right) --> and return the best one

if target < v:
  ---> look at candidates = (v, recursive ans on node.right) --> and return the best one

bugs to watch out for :

best one = min distance = abs(value-target)


edge case:

if there are multiple values equidistant from target, need to return the smallest one

