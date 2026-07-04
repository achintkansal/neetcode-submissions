class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []
        def helper_comb_sum(curr_sum, i, curr_res):

            if curr_sum == target:
                self.res.append(curr_res.copy())
                return
            
            if (curr_sum > target) or (i == len(nums)):
                return
            
            curr_res.append(nums[i])
            helper_comb_sum(curr_sum + nums[i], i, curr_res) ## consider the element
            curr_res.pop()
            helper_comb_sum(curr_sum, i+1, curr_res) ## do not consider element
        
        helper_comb_sum(0, 0, [])
        return self.res
        