# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        i = 0
        j = 1

        while j < len(nums):
            while nums[i] == nums[j]:
                j += 1
                if j >= len(nums):
                    break

            if j >= len(nums):
                break

            nums[i + 1] = nums[j]

            i += 1
            j += 1


        return i + 1
