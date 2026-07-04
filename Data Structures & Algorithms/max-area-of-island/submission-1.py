class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]

        self.count_islands = 0
        self.curr_count = 0

        def dfs(i, j):
            
            if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or (grid[i][j] == 0):
                return

            self.curr_count += 1

            grid[i][j] = 0
            for d in range(4):
                new_i = i + dir_x[d]
                new_j = j + dir_y[d]

                dfs(new_i, new_j)

            return

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    self.curr_count = 0
                    dfs(i,j)
                    self.count_islands = max(self.count_islands, self.curr_count)
        
        return self.count_islands

        