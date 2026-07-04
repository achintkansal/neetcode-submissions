class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates.copy()
        self.res = []
        subres = []
        n = len(candidates)

        def helper_comb(rem_sum, start):
            
            if rem_sum == 0:
                self.res.append(subres.copy())
                return

            if rem_sum < 0:
                return
            

            for i in range(start, n):

                if (i > start) and (nums[i-1] == nums[i]):
                    continue
                subres.append(nums[i])
                helper_comb(rem_sum-nums[i], i+1)
                subres.pop()

        helper_comb(target, 0)
        return self.res