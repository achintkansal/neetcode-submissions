class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        subset = []
        res = []
        def helper(open, close):

            if open == 0 and close == 0:
                res.append("".join(subset))
                return
            
            if (open > close):
                return
            
            if open > 0:
                subset.append('(')
                helper(open-1, close)
                subset.pop()

            if close > 0:
                subset.append(')')
                helper(open, close-1)
                subset.pop()
        
        helper(n, n)
        return res
            

        