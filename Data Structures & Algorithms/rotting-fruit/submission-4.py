class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_n, col_n = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        grid1 = grid.copy()

        visited = [False] * (row_n * col_n)

        queue = deque()
        
        def find_index(r , c):
            return (r * col_n + c)

        def bfs():
            
            depth = -1
            while len(queue) > 0:

                n = len(queue)
                
                for i in range(n):
                    r, c = queue.popleft()
                    visited[find_index(r, c)] = True
                    for d in range(4):
                        new_r = r + dx[d]
                        new_c = c + dy[d]

                        if (new_r < 0) or (new_c < 0) or (new_r >= row_n) or (new_c >= col_n) or (grid1[new_r][new_c] == 0) or (grid1[new_r][new_c] == 2) or (visited[find_index(new_r, new_c)]):
                            continue
                        
                        grid1[new_r][new_c] = 2
                        queue.append((new_r, new_c))

                depth += 1
            return depth
        
        for i in range(row_n):
            for j in range(col_n):

                if grid[i][j] == 2:
                    queue.append((i,j))
        
        depth = bfs()
        
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j] == 1:
                    return -1

        return depth if depth > 0 else 0


        