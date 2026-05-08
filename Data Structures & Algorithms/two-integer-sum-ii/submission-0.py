class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums) - 1
        i = 0

        while i < j:
            _sum = nums[i] + nums[j]
            if _sum == target:
                return [i+1,j+1]
            elif _sum > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]
