class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)

        while (i < n):

            while (i != nums[i]) and (nums[i] < n):
                k = nums[i]
                nums[k], nums[i] = nums[i], nums[k]
            i += 1

        for i in range(n):
            if nums[i] != i:
                return i
        return n

        