class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices: #selling price
            profit = max(profit, i - buy)
            buy = min(buy, i)

        return profit
        