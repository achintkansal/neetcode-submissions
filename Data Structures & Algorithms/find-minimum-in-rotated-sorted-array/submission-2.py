class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n-1

        ## rule is left is always less than right
        ## if mid > mid+1 return mid + 1
        ## if the above condition is not satisfed for any of the combination return nums[0]

        while left <= right:
            mid = left + ((right - left) // 2)

            if (mid < n-1) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[0]
        
        