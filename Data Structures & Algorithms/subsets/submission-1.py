class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def helper(i):

            if i >= len(nums):
                print(curr)
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            #print(curr)
            helper(i+1)
            curr.pop()
            helper(i+1)

        helper(0)
        return res


        