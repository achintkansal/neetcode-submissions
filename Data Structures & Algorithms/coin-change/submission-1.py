class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[-1]*(n+1) for i in range(amount+1)]

        def helper(curr_amt, curr_loc):
            
            if curr_amt == 0:
                return 0
            
            if (curr_loc == n) or (curr_amt < 0):
                return float('inf')
            
            if dp[curr_amt][curr_loc] != -1:
                return dp[curr_amt][curr_loc]
            
            take = 1 + helper(curr_amt - coins[curr_loc], curr_loc)
            not_take = helper(curr_amt, curr_loc+1)

            dp[curr_amt][curr_loc] = min(take, not_take)
            return dp[curr_amt][curr_loc]
        
        res = helper(amount, 0)
        if res == float('inf'):
            return -1
        return res