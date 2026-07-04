class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        hs = set(wordDict)
        
        n = len(s)
        dp =[-1] * (n+1)

        def helper(start):

            if (start == n):
                return True

            if dp[start] != -1:
                return dp[start]

            for word in wordDict:
                
                if (len(word) + start <= len(s)) and (s[start: start+len(word)] == word):
                    res =  helper(start + len(word))
                    dp[start] = res
                    if res:
                        return dp[start]
            
            return False


        
        return helper(0)
        