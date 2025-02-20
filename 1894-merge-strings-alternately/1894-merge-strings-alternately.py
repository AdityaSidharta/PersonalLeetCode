class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 == "":
            return word2
        elif word2 == "":
            return word1
        else:
            word1_len = len(word1)
            word2_len = len(word2)
            word_len = min(word1_len, word2_len)
            merged = ""
            for idx in range(word_len):
                merged = merged + word1[idx]
                merged = merged + word2[idx]
            if word1_len > word2_len:
                merged = merged + word1[word_len:]
            else:
                merged = merged + word2[word_len:]
            return merged