class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(n-1, -1, -1):
            for j in range(amount+1):
                
                take = float('inf')
                if (j - coins[i]) >= 0:
                    take = 1 + dp[i][j - coins[i]]
                nottake = dp[i+1][j]

                dp[i][j] = min(take, nottake)
        print(dp)
        
        if dp[0][amount] == float('inf'):
            return -1
        return dp[0][amount] 