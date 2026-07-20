class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for num in range(n+1): ## solution 32*n time solution

            i = num
            count = 0
            while i > 0:
                count += 1
                i = i & (i-1)
            res.append(count)
        
        return res
            
        