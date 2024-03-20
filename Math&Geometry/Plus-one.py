# To revise at some point 

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        index = len(digits) - 1
        while index >= 0:
            d = digits[index] + 1
            if d == 10:
                digits[index] = 0
                index -=1
                if index < 0:
                    digits = [1] + digits
            else:
                digits[index] = d
                index = -1

        return digits
