class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        res = -1
        n = len(nums)
        cntk = 0
        for val in nums:
            if val == k:
                cntk += 1

        
        global_max = float('-inf')
        for num in range(1,51):
            curr_sum = 0
            val = 0
            for i in range(n):
                
                if nums[i] == num:
                    val = 1
                    curr_sum += 1
                
                if nums[i] == k:
                    val = -1
                    curr_sum -= 1
                
                curr_sum = max(curr_sum, val)
                global_max = max(global_max, curr_sum)
                val = 0
            print(num, global_max)
        return max(global_max,0) + cntk




        