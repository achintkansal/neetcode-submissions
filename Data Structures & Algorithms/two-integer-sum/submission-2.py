class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## to find index we will use dictionary
        hm = {}

        n = len(nums)
        for i in range(n):
            k = target - nums[i]
            if k in hm:
                return [hm[k], i]
            else:
                hm[nums[i]] = i
        
        