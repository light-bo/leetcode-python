
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry_bit = 0

        for index in range(len(digits) - 1, -1, -1):
            temp_val = 0

            if index == (len(digits) - 1):
                temp_val = digits[index] + carry_bit + 1
            else:
                temp_val = digits[index] + carry_bit

            if temp_val < 10:
                carry_bit = 0
                digits[index] = temp_val
                break
            else:
                carry_bit = 1
                digits[index] = temp_val - 10

        if carry_bit != 0:
            digits.insert(0, 1)

        return digits
