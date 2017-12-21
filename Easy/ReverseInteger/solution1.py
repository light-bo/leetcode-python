# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within
# the 32-bit signed integer range. For the purpose of this problem, assume that your
# function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        isNegative = 0

        if x < 0:
            x = -x
            isNegative = 1

        if x == 0:
            return 0


        while x % 10 == 0:
            x /= 10

        while x > 0:
            temp = x % 10

            if result == 0:
                result = temp
            else:
                result = result * 10 + temp
                if (result >= (2 ** 31 - 1)):
                    return 0

            x = int(x / 10)

        if isNegative:
            result = - result


        return int(result)
