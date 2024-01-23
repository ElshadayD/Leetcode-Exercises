# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

class Solution(object):
    def plusOne(self, digits):
        x = len(digits) - 1
        while x >= 0:
            if digits[x] == 9:
                digits[x] = 0
                x -= 1
            else:
                digits[x] += 1
                return digits

        digits.insert(0, 1)
        return digits
