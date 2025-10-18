class Solution:
    def isVowel(self, alphabet):
        return alphabet in 'AIUEOaiueo'
    def reverseVowels(self, s: str) -> str:     
        s = list(s)
        if len(s) == 1:
            return ''.join(s)
        else:
            l = 0
            r = len(s) - 1
            while l < r:
                if self.isVowel(s[l]) and self.isVowel(s[r]):
                    s[l], s[r] = s[r], s[l]
                    l = l + 1
                    r = r - 1
                elif self.isVowel(s[l]):
                    r = r -1
                elif self.isVowel(s[r]):
                    l = l + 1
                else:
                    l = l + 1
                    r = r - 1
        return ''.join(s)