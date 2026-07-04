class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [-1] * n
        dp2 = [-1] * n

        if len(nums) == 1:
            return nums[0]
        def helper(i, j, dp):

            if i >= j:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            rob = nums[i] + helper(i+2, j,dp)
            not_rob = helper(i+1, j, dp)

            dp[i] = max(rob, not_rob)
            return dp[i]
        
        return max(helper(0,n-1,dp1), helper(1, n,dp2))