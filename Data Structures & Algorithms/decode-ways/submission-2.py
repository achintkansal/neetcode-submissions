class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.mapad = {}
        for i in range(26):
            self.mapad[str(i+1)] = chr(i+65)
        
        n = len(s)
        dp = [[-1]*(n+1) for i in range(n+1)]

        def helper(start, end):

            if start == n and end == n:
                # self.no_of_ways += 1
                return 1
            
            if start == n or end == n:
                return 0
            
            if dp[start][end] != -1:
                return dp[start][end]

            if s[start:end+1] in self.mapad:
                take = helper(end+1, end+1) ## Take that character and find other ways
                nottake = helper(start, end+1) ## Don't take that character and find if other is possible

                dp[start][end] = take+nottake
                return dp[start][end]
            
            return 0
        
        
        return helper(0,0)