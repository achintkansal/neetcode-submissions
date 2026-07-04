class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        subset = []
        n = len(s)
        def helper(start, end):

            if (start == n) and (end == n):
                res.append(subset.copy())
                return
            if (start == n) or (end == n):
                return
            
            if isPalindrome(s[start:end+1]):
                subset.append(s[start:end+1])
                helper(end+1, end+1)
                subset.pop()
            
            helper(start, end+1)
        
        helper(0, 0)
        return res

        

        