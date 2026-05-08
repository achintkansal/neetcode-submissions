class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = -1
        min_buy = float('inf')
        n = len(prices)

        for i in range(n):
            if prices[i] < min_buy:
                min_buy = prices[i]
            
            profit = prices[i] - min_buy
            max_profit = max(max_profit, profit)
        
        return max_profit
        