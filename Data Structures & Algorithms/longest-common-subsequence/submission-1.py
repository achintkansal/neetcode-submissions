class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        dp = {}
        def helper(i, j):

            if i < 0 or j < 0:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if text1[i] == text2[j]:
                dp[(i,j)] =  1 + helper(i-1, j-1)
            
            else:
                dp[(i,j)] =  max(helper(i-1, j), helper(i, j-1))
            
            return dp[(i,j)]

        return helper(m-1, n-1)