class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        def helper():

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    helper()
                    subset.pop()
        helper()
        return res

        