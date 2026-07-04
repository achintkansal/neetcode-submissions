class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        min_sum = float('inf')

        curr_max = float('-inf')
        curr_min = float('inf')
        
        total = sum(nums)
        n = len(nums)
        for i in range(n):

            curr_max = max(curr_max+nums[i], nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min+nums[i], nums[i])
            min_sum = min(min_sum,curr_min)

        if total == min_sum:
            return max_sum
        return max(max_sum, total - min_sum)
        