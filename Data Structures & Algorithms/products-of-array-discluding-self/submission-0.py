class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## prefix prod array
        ## postfix prod array
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        prod = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(n):

            prod[i] = (prefix[i]) * (postfix[i])
        print(prefix)
        print(postfix)
        return prod

            
    
# 3 4 5 6

# 1 3 12 60
# 120  30 6  1


        