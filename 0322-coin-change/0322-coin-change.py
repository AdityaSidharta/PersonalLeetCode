class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        results = [-1] * amount
        for i in range(len(results)):
            target = i + 1
            if target in coins:
                results[i] = 1
            else:
                min_coins = -1
                for j in coins:
                    if i - j < 0:
                        continue
                    elif results[i - j] < 0:
                        continue
                    else:
                        if min_coins == -1:
                            min_coins = results[i - j] + 1
                        else:
                            min_coins = min(min_coins, results[i - j] + 1)
                results[i] = min_coins
        return results[-1]

