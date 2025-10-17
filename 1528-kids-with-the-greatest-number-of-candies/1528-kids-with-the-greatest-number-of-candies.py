class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = 0
        n = len(candies)
        for i in range(n):
            if candies[i] > max_:
                max_ = candies[i]
        result = []
        for i in range(n):
            if max_ - extraCandies > candies[i]:
                result.append(False)
            else:
                result.append(True)
        return result