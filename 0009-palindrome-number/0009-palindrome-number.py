class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x < 10:
            return True
        else:
            reversed = 0
            while reversed < x:
                reversed = reversed * 10 + x % 10
                x = x // 10
            return reversed == x or reversed // 10 == x