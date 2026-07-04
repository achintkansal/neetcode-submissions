class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.rank[a] < self.rank[b]: a, b = b, a
        self.p[b] = a
        if self.rank[a] == self.rank[b]: self.rank[a] += 1
        return True

    def same(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def find_index(r,c):
            return (r*cols + c)
        
        n = rows*cols
        dsu = DSU(n)

        island = 0
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for r in range(rows):
            for c in range(cols):
                 if grid[r][c] == "1":
                    island += 1
                
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "0":
                    continue

                curr_index = find_index(r,c)

                for d in range(4):
                    new_r = r + dx[d]
                    new_c = c + dy[d]

                    if (new_r < 0) or (new_c < 0) or (new_r >= rows) or (new_c >= cols) or (grid[new_r][new_c] == "0"):
                        continue

                    if dsu.union(find_index(new_r, new_c), curr_index):
                        island -= 1
                    
                        
        return island  
                        
                    

                    

                


















