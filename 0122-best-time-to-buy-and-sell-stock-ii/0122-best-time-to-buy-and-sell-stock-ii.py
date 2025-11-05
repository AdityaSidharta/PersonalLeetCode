class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_holding = -1
        for price in prices:
            if current_holding == -1:
                current_holding = price
            else:
                if current_holding < price:
                    profit = profit + price - current_holding
                current_holding = price
        return profit