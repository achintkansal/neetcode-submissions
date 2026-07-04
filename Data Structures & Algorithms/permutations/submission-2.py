class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
        pick = [False] * len(nums)
        def helper():

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    pick[i] = True
                    subset.append(nums[i])

                    helper()

                    subset.pop() ## backtracking
                    pick[i] = False ## backtracking
        helper()
        return res

        