class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        subset = []
        res = []
        def helper(open, close):

            if open == 0:
                for i in range(close):
                    subset.append(')')
                res.append("".join(subset))
                for i in range(close):
                    subset.pop()
                return
            
            if (close == 0) or (open > close):
                return
            
            subset.append('(')
            helper(open-1, close)
            subset.pop()

            subset.append(')')
            helper(open, close-1)
            subset.pop()
        
        helper(n, n)
        return res
            

        