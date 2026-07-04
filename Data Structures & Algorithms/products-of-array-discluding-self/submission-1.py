class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pref_prod = [1] * n
        suf_prod = [1] * n

        for i in range(1, n):
            pref_prod[i] = pref_prod[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suf_prod[i] = suf_prod[i+1] * nums[i+1]
        
        output = [0] * n

        for i in range(n):
            output[i] = pref_prod[i] * suf_prod[i]
        
        return output
        