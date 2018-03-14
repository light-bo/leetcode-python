# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None:
            return None

        map_one = {}
        map_two = {}
        result = list()

        for val in nums1:
            if val in map_one:
                map_one[val] += 1
            else:
                map_one[val] = 1

        for val in nums2:
            if val in map_two:
                map_two[val] += 1
            else:
                map_two[val] = 1

        for val in nums1:
            if val in map_one and val in map_two:
                if map_one[val] != 0 and map_two[val] != 0:
                    result.append(val)

                    map_one[val] -= 1
                    map_two[val] -= 1

        return result
