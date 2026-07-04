class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [[-1] * (n+1) for i in range(n+1)]

        def helper(prev_index, index):

            if index == n:
                return 0
            
            if dp[prev_index+1][index] != -1:
                return dp[prev_index+1][index]
                
            take = 0
            if (prev_index == -1) or (nums[prev_index] < nums[index]):
                take = 1 + helper(index, index + 1)
            
            not_take = helper(prev_index, index+1)

            dp[prev_index+1][index] = max(take, not_take)
            return dp[prev_index+1][index]
        
        return helper(-1, 0)
        