class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        self.res = []
        def helper_subsets(arr, i):

            if i == n:
                self.res.append(arr.copy())
                return
            
            arr.append(nums[i])
            helper_subsets(arr, i+1)
            arr.pop()
            helper_subsets(arr, i+1)
        
        helper_subsets([], 0)
        return self.res
        