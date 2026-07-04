class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        f_max = 1
        g_min = 1
        res = float('-inf')

        for i in range(len(nums)):
            
            f_maxc = f_max
            g_minc = g_min
            
            f_max = max(f_maxc*nums[i], g_minc*nums[i], nums[i])
            g_min = min(f_maxc*nums[i], g_minc*nums[i], nums[i])

            res = max(f_max, g_min, res)
        
        return res
        