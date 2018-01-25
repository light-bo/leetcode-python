# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and nums[j]
# is at most t and the absolute difference between i and j is at most k.
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 1 or k <= 0:
            return False

        low = 0
        # maintain a sliding window
        s = set()

        for i in range(0, len(nums)):
            if i - low > k:
                s.remove(nums[low])
                low += 1

            key = self.lowerBound(s, nums[i] - t)
            if key is not None and abs(key - nums[i]) <= t:
                return True

            s.add(nums[i])

        return False

    def lowerBound(self, s, val):
        for item in s:
            if item >= val:
                return item

        return None
