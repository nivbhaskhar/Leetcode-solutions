#https://leetcode.com/problems/nested-list-weight-sum/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depth_sum_recursive(self, nested_list:list[NestedInteger], current_depth: int)->int:
        depth_sum = 0
        for member in nested_list:
            if member.isInteger():
                depth_sum += current_depth*member.getInteger()
            else:
                prev_depth_sum = self.depth_sum_recursive(member.getList(), current_depth+1)
                depth_sum += prev_depth_sum
        return depth_sum


    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        if len(nestedList) == 0:
            return 0

        return self.depth_sum_recursive(nestedList, 1)
        
