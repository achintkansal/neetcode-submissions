class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i in range(len(nums)):
            t = target - nums[i]
            if t in ind:
                return [ind[t], i]
            ind[nums[i]] = i
        
        return []
        



        