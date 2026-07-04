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

        