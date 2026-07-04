class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        water = -1
        chest = 0
        
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, -1, 1]
        row_n, col_n = len(grid), len(grid[0])

        def find_shortest_path_dfs(row, col):
            if (row < 0) or (col < 0) or (row >= row_n) or (col >= col_n) or (grid[row][col] == water) or (grid[row][col] == -2):
                return float('inf') 

            if grid[row][col] == chest:
                return 0
            
            count_path = float('inf')
            
            temp = grid[row][col]
            grid[row][col] = -2

            for d in range(4):
                new_r = row + dir_x[d]
                new_c = col + dir_y[d]

                count_path = min(count_path, 1 + find_shortest_path_dfs(new_r, new_c))
            
            grid[row][col] = temp
            return count_path

        def find_index(row, col):
            return (row * col_n + col)
        
        visited = [False] * (row_n * col_n)
        def find_shortest_path_bfs(row, col):

            depth = -1
            queue = deque()
            queue.append((row,col))

            while len(queue) > 0:

                n = len(queue)
                depth += 1
                for i in range(n):
                    r, c = queue.popleft()
                    
                    visited[find_index(r,c)] = True
                    if grid[r][c] == chest:
                        return depth
                    
                    for d in range(4):
                        new_r = r + dir_x[d]
                        new_c = c + dir_y[d]

                        if (new_r < 0) or (new_c < 0) or (new_r >= row_n) or (new_c >= col_n) or (grid[new_r][new_c] == water) or (visited[find_index(new_r,new_c)]):
                            continue
                        
                        queue.append((new_r, new_c))
            
            return land     
        
        for i in range(row_n):
            for j in range(col_n):

                if grid[i][j] == land:
                    visited = [False] * (row_n * col_n)
                    grid[i][j] = find_shortest_path_bfs(i,j)
        
        