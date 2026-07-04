class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ## for pacific:
        ## row < 0 or col < 0 ; up or left

        ## for atlantic 
        ## row >= row_n or col >= col_n ; down or right

        row_n = len(heights)
        col_n = len(heights[0])

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        visited = set()

        self.pacific = False
        self.atlantic = False

        def dfs(prev, r,c):
            
            if (r < 0) or (c < 0):
                self.pacific = True
                return
            
            if (r >= row_n) or (c >= col_n):
                self.atlantic = True
                return

            if prev < heights[r][c]:
                return

            visited.add((r,c))
            for i in range(4):

                new_r = r + dx[i]
                new_c = c + dy[i]

                if self.atlantic and self.pacific:
                    return
                
                if (new_r, new_c) not in visited:
                    dfs(heights[r][c], new_r, new_c)
            
        
        res = []
        for i in range(row_n):
            for j in range(col_n):
                visited = set()
                self.pacific = False
                self.atlantic = False

                dfs(float('inf'),i,j)

                if self.pacific and self.atlantic:
                    res.append([i,j])
        
        return res


        