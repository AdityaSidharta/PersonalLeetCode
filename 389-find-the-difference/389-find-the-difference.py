class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for idx in range(len(s)):
            result = result ^ ord(s[idx])
        for idx in range(len(t)):
            result = result ^ ord(t[idx])
        return chr(result)