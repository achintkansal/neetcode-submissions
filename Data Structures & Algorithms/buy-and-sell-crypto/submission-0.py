class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy_min = prices[0]
        for sell in prices:
            profit = max(profit, sell - buy_min)
            buy_min = min(buy_min, sell)
        

        return profit
        