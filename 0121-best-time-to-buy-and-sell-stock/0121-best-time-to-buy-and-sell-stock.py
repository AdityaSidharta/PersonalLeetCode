class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = -1
        current_profit = 0
        best_profit = 0
        for price in prices:
            if current == -1:
                current = price
            else:
                if price - current > current_profit:
                    current_profit = price - current
                else:
                    if price < current:
                        current = price
                        best_profit = max(best_profit, current_profit)
                        current_profit = 0
        return max(best_profit, current_profit)
