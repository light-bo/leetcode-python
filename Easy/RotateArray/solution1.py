# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 1:
            return

        if k <= 0:
            return

        temp_nums = []
        for val in nums:
            temp_nums.append(val)

        for index in range(0, len(temp_nums)):
            rotate_index = (index + k) % len(temp_nums)
            nums[rotate_index] = temp_nums[index]
