# Given an array and a value, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        head = 0
        tail = len(nums) - 1

        while head <= tail:
            if nums[head] == val:
                temp = nums[head]
                nums[head] = nums[tail]
                nums[tail] = temp

                tail -= 1
            else:
                head += 1

        return head
