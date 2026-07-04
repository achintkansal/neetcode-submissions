class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for i in range(n)]
        print(board)
        def check_place(row, col):

            ## check horizontally
            for i in range(n):
                if (i != col) and board[row][i] == 'Q':
                    return False
            ## check vertical
            for i in range(n):
                if (i != row) and board[i][col] == 'Q':
                    return False
            ## diagonals
            dx = [1, -1, 1, -1]
            dy = [1, -1, -1, 1]
            
            for i in range(4):
                r = row + dx[i]
                c = col + dy[i]
                while (r>=0) and (c>=0) and (r<n) and (c<n):
                    if board[r][c] == 'Q':
                        return False
                    r = r + dx[i]
                    c = c + dy[i]
            return True
        dx = [1, -1, 1, -1, 0, 0, 1, -1]
        dy = [1, -1, -1, 1, 1, -1, 0, 0]
        res = []
        def helper(row, col):

            if col == n:
                subset = []
                for k in range(n):
                    subset.append("".join(board[k]))
                res.append(subset)
            if row < 0 or col < 0 or row >= n or col >= n:
                return False
            
            for i in range(n):
                board[i][col] = 'Q'
                if check_place(i,col):
                    helper(0, col + 1)
                board[i][col] = '.'

        helper(0,0)
        return res
        