class Solution:
    def countBits(self, n: int) -> List[int]:

        offset = 1
        res = [0] * (n+1)
        
        for i in range(1,n+1): ## O(n) time solution
            offset = (2*offset) if (2*offset) == i else offset
            res[i] = 1 + res[i-offset]
        
        return res
        
            
        