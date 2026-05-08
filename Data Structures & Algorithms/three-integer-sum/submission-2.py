class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                _sum = nums[k] + nums[i] + nums[j]
                if _sum == 0:
                    print('hi')
                    if [nums[k],nums[i],nums[j]] not in ans:
                        ans.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                elif _sum > 0:
                    j -= 1
                else:
                    i += 1
        
        return ans


        