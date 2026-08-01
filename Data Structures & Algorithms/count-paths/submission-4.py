class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ### direct combination question: m+n-2 C n-1 or m+n-2 C m-1
        ### = (m * m+1 * m+2 * m + n - 2) / (n-1)!

        res = 1
        if n > m: ## If this part was not there then time complexity is O(n), but with this it is O(min(m,n))
            m, n = n, m

        for i in range(m, m+n-1): ## TC: O(n)
            res *= i
            res //= i - m + 1
        
        return res

        
        # dp = {}
        # def helper_paths(i,j):

        #     if (i >= m) or (j >= n):
        #         return 0
            
        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     right = helper_paths(i, j+1)
        #     down = helper_paths(i+1, j)

        #     dp[(i,j)] = (down+right)
        #     return dp[(i,j)]
        
        # return helper_paths(0,0)
        