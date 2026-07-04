class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]

        
        def dfs(i, j):

            grid[i][j] = 0
            ans = 1
            for d in range(4):
                new_i = i + dir_x[d]
                new_j = j + dir_y[d]

                if (new_i >= 0) and (new_i < len(grid)) and (new_j >= 0) and (new_j < len(grid[0])) and (grid[new_i][new_j] == 1):
                    ans += dfs(new_i, new_j)  

            return ans

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    ans = dfs(i,j)
                    res = max(ans, res)
                    
        
        return res

        