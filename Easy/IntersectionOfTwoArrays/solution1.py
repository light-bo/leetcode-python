# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None:
            return nums2

        if nums2 is None:
            return nums1

        list_one_set = set(nums1)
        result_set = set()

        for val in nums2:
            if val in list_one_set:
                result_set.add(val)

        return list(result_set)
