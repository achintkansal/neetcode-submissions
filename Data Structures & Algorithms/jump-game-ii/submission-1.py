class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jumps = 0
        jump_pointer, i = 0, 0
        n = len(nums)

        while i <= jump_pointer and i < n:

            if jump_pointer >= (n-1):
                return min_jumps

            jumps = i + nums[i]
            if jumps > jump_pointer:
                jump_pointer = jumps
                min_jumps += 1
            
            i += 1
        
        return -1

    # [2, 1, 2, 1, 0] # n-1 = 4
    # jumps = 4
    # jump_pointer = 4
    # min_jumps = 2
        