# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 1:
#
# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        index = self.findVal(nums, target, 0, len(nums))

        return index



    def findVal(self, nums, val, begin, end):
        if end <= begin:
            return begin

        middle = int((end + begin) / 2)
        if val == nums[middle]:
            return middle
        elif val < nums[middle]:
            return self.findVal(nums, val, begin, middle)
        else:
            return self.findVal(nums, val, middle + 1, end)
