class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        else:
            idxs = 0
            idxt = 0
            lens = len(s)
            lent = len(t)
            while (idxt < lent) and (idxs < lens):
                if s[idxs] == t[idxt]:
                    idxs = idxs + 1
                    idxt = idxt + 1
                else:
                    idxt = idxt + 1
            print(idxs, idxt)
            return idxs == lens