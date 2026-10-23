import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = math.inf
        high = -1
        for i in range(len(prices) - 1):
            if prices[i] < low:
                low = prices[i]
                high = -1
            if prices[i + 1] > high:
                high = prices[i + 1]
            profit = max(profit, high - low)
        return profit