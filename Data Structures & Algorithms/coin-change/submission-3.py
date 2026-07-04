class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        # dp = [[float('inf')]*(amount+1) for i in range(n+1)]

        curr = [float('inf')]*(amount+1)
        prev = [float('inf')]*(amount+1)

        # for i in range(n+1):
        #     dp[i][0] = 0
        
        curr[0] = 0
        prev[0] = 0

        for i in range(n-1, -1, -1):
            for j in range(amount+1):
                
                take = float('inf')
                if (j - coins[i]) >= 0:
                    take = 1 + curr[j - coins[i]]
                nottake = prev[j]

                prev = curr.copy()
                curr[j] = min(take, nottake)
        
        if curr[amount] == float('inf'):
            return -1
        return curr[amount] 