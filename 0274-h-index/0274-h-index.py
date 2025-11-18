class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        counts = [0] * length
        for cit in citations:
            if cit > 0:
                counts[min(cit-1, length-1)] += 1
        hindex = length
        while hindex > 0:
            if counts[hindex - 1] >= hindex:
                break
            if hindex >= 2:
                counts[hindex - 2] += counts[hindex - 1]
            hindex -= 1
        return hindex