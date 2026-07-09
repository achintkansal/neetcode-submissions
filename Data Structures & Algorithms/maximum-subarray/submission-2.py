class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ## kadane's algorithm
        glob_sum = float('-inf')
        local_sum = float('-inf')

        for num in nums:

            local_sum = max(local_sum + num, num) ## either include the curr_element in sum or directly take the curr element
            glob_sum = max(glob_sum, local_sum)
        
        return glob_sum

        