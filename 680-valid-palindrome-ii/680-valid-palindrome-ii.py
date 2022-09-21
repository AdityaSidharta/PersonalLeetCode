from functools import lru_cache

class Solution(object):
    
    def isPalindrome(self, s):
        reverse_string = s[::-1]
        return s == reverse_string
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
            else:
                break
        if (i == j) or (i > j):
            return True
        else:
            if (self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])):
                return True
            else:
                return False