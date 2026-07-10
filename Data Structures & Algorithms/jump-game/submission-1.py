class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_pointer = 0
        i = 0

        while (i <= jump_pointer) and (i < len(nums)): 
            jump_pointer = max(jump_pointer, nums[i] + i) ## extending the possible window
            if jump_pointer >= (len(nums)-1): ## if window exceeds the length of nums return true
                return True
            
            i += 1
        
        return False
        
        # 1 2 0 1 0
        #   j 