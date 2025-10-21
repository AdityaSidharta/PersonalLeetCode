class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        le = len(digits)
        r = le - 1
        while r >= 0:
            if digits[r] + remainder == 10:
                digits[r] = 0
                remainder = 1
                r = r -1 
            else:
                digits[r] = digits[r] + remainder
                remainder = 0
                r = r - 1
        if remainder == 1:
            return [1] + digits
        else:
            return digits