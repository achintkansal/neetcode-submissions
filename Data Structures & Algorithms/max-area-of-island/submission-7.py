class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: 
            return False
        if self.size[a] < self.size[b]: 
            a, b = b, a
        self.p[b] = a
        if self.size[a] == self.size[b]: 
            self.size[a] += 1
        else:
            self.size[a] += self.size[b]
        return True

    def r_size(self, a): 
        return self.size(self.find(a))
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]

        rows = len(grid)
        cols = len(grid[0])

        flag = False
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    flag = True


        def index(r, c):
            return (r * cols + c)

        dsu = DSU(rows*cols)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    continue
                
                for d in range(4):
                    n_r = r + dir_x[d]
                    n_c = c + dir_y[d]

                    if (n_r < 0) or (n_c < 0) or (n_r >= rows) or (n_c >= cols) or (grid[n_r][n_c] == 0):
                        continue
                    
                    dsu.union(index(n_r, n_c), index(r, c))
        if flag:
            return max(dsu.size)
        else:
            return 0



        