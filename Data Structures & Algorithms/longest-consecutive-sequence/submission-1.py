class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_found = 0
        for num in nums:
            count = 1
            if (num - 1) not in unique:
                while True:
                    if (num + count) in unique:
                        count += 1
                    else:
                        break
                max_found = max(max_found, count)
        return max_found
                    




        