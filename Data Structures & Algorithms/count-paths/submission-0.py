class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper_paths(i,j):

            if (i >= m) or (j >= n):
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            right = helper_paths(i, j+1)
            down = helper_paths(i+1, j)

            return (down+right)
        
        return helper_paths(0,0)
        