# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2 or k < 1:
            return False

        dict = {}

        for index in range(0, len(nums)):
            val = nums[index]

            if val in dict:
                l = dict[val]
                l.append(index)

                if abs(l[len(l) - 1], l[len(l) - 2]) <= k:
                    return True
            else:
                l = []
                l.append(index)
                dict[val] = l

        return False
