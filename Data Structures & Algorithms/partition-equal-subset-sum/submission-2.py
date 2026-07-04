class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        
        target = _sum // 2
        n = len(nums)

        dp = [[-1] * (target+1) for _ in range(n)]

        def helper(index, target_sum):

            if target_sum == 0:
                return True
            
            if (index == n) or (target_sum < 0):
                return False
            
            if dp[index][target_sum] != -1:
                return dp[index][target_sum]

            take = False
            if (target_sum - nums[index]) >= 0:
                take = helper(index+1, target_sum - nums[index])
            
            not_take = helper(index+1, target_sum)

            dp[index][target_sum] = (take or not_take)

            return dp[index][target_sum] 
        
        return helper(0, target)


