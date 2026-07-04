class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        self.res = []
        def helper_subsets(arr, i):

            if i == n:
                self.res.append(arr.copy())
                return
            
            
            helper_subsets(arr, i+1) ##include arr[i]
            arr.append(nums[i])
            helper_subsets(arr, i+1) ## exclude arr[i]
            arr.pop()
            
        helper_subsets([], 0)
        return self.res
        