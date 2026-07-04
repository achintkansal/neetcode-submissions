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
        # visited = set()

        self.pacific = set()
        self.atlantic = set()

        def dfs(prev, r,c, true_pacific):
            
            if (r < 0) or (c < 0) or (r >= row_n) or (c >= col_n) or (prev > heights[r][c]):
                return
            
            if true_pacific and (r,c) in self.pacific:
                return
            
            if not true_pacific and (r,c) in self.atlantic:
                return
            
            if prev <= heights[r][c]:
                if true_pacific:
                    self.pacific.add((r,c))
                else:
                    self.atlantic.add((r,c))

            # visited.add((r,c))
            for i in range(4):

                new_r = r + dx[i]
                new_c = c + dy[i]
                
                dfs(heights[r][c], new_r, new_c, true_pacific)
            
        
        
        for i in range(row_n):
            for j in range(col_n):
                # visited = set()
                
                if (i == 0) or (j == 0):
                    # print('index:', i,j)
                    dfs(float('-inf'),i,j, True)

                visited = set()

                if (i == row_n-1) or (j == col_n-1):
                    # print('index:', i,j)
                    dfs(float('-inf'),i,j, False)
        print(self.pacific)
        print(self.atlantic)
        res = list(self.pacific & self.atlantic)
        return res


        