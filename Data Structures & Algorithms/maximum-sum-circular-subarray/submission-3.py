class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum = -30001
        n = len(nums)
        for i in range(n):
            curr_sum = 0
            for j in range(n):
                curr_sum += nums[(i+j)%n]
                max_sum = max(curr_sum, max_sum)
        
        return max_sum

                
        