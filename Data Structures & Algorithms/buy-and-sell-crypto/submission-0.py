class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if profit > maxProfit:
                maxProfit = profit
            if prices[i] < buy:
                buy = prices[i]

        return maxProfit