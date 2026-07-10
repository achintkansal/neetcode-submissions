class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jumps = 0
        l,r = 0, 0
        n = len(nums)

        while l <= r and l < n:

            if r >= (n-1):
                return min_jumps

            farthest_jump = 0
            for i in range(l,r+1):
                farthest_jump = max(farthest_jump, i + nums[i])
            
            min_jumps += 1
            
            l = r+1
            r = farthest_jump
            
        return -1

    # [2, 1, 2, 1, 0] # n-1 = 4
    # jumps = 4
    # jump_pointer = 4
    # min_jumps = 2
        