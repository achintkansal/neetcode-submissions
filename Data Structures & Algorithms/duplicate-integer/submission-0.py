class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicates = set()

        for num in nums:
            if num in check_duplicates:
                return True
            check_duplicates.add(num)
        
        return False
        