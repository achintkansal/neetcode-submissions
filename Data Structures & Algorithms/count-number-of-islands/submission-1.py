class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]

        def dfs(i, j):
            
            if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or (grid[i][j] == "0"):
                return
                 
            grid[i][j] = "0"
            for d in range(4):
                dfs(i + dir_x[d], j + dir_y[d])

        count_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (grid[i][j] == "1"):
                    dfs(i,j)
                    count_islands += 1
        
        return count_islands
