class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n
        def helper(i):

            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]
            rob = nums[i] + helper(i+2)
            not_rob = helper(i+1)

            dp[i] = max(rob, not_rob)
            return dp[i]
        
        return helper(0)
        