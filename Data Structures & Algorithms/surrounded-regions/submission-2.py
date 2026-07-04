class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row_n = len(board)
        col_n = len(board[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        visited = set()
        def dfs(r,c):

            if (r < 0) or (c < 0) or (r == row_n) or (c == col_n) or (board[r][c] == 'X'):
                return
            
            board[r][c] = '*'
            visited.add((r,c))
            for i in range(4):
                new_r = r + dx[i]
                new_c = c + dy[i]

                if (new_r, new_c) not in visited:
                    dfs(new_r,new_c)



        for c in range(col_n):
            
            if (board[0][c] == 'O') or (board[0][c] == '*'):
                visited = set()
                dfs(0,c)
                # i = 0
                # while (i < row_n) and ((board[i][c] == 'O') or (board[i][c] == '*')):
                #     board[i][c] = '*'
                #     i += 1

            
            if (board[row_n-1][c] == 'O') or (board[row_n-1][c] == '*'):
                visited = set()
                dfs(row_n-1,c)
                # i = row_n-1
                # while (i >= 0) and ((board[i][c] == 'O') or (board[i][c] == '*')):
                #     board[i][c] = '*'
                #     i -= 1
        
        for r in range(row_n):
            if (board[r][0] == 'O') or (board[r][0] == '*'):
                visited = set()
                dfs(r,0)
                # j = 0
                # while (j < col_n) and ((board[r][j] == 'O') or (board[r][j] == '*')):
                #     board[r][j] = '*'
                #     j += 1
            
            if (board[r][col_n-1] == 'O') or (board[r][col_n-1] == '*'):
                visited = set()
                j = col_n-1
                dfs(r, col_n-1)
                # print(r,j, board[r][j])
                # while (j >= 0) and ((board[r][j] == 'O') or (board[r][j] == '*')):
                #     print(r, j, board[r][j])
                #     board[r][j] = '*'
                #     j -= 1
        print(board)
        for i in range(row_n):
            for j in range(col_n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(row_n):
            for j in range(col_n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
