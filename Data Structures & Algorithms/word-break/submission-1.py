class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        hs = set(wordDict)
        
        n = len(s)
        dp =[ [-1] * (n) for _ in range(n)]
        def helper(start, end):

            if (start == n) and (end == n):
                return True
            
            if (start == n) or (end == n):
                return False
                
            if dp[start][end] != -1:
                return dp[start][end]

            take = False
            if s[start:end+1] in hs:
                take = helper(end+1, end+1)
            
            not_take = helper(start, end+1)
            dp[start][end] = take or not_take
            return dp[start][end]


        
        return helper(0,0)
        