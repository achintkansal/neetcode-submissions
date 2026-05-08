class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append(nums)
        def helper(nums, i):
            while i < len(nums):
                subset = [nums[k] for k in range(len(nums)) if k != i]
                if subset not in ans:
                    ans.append(subset)
                helper(subset, i)
                i += 1
        helper(nums,0)
        print(ans)
        return ans


        