class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, -1, 1]

        n = len(word)
        def helper(row, col, pos):

            if pos == n:
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if word[pos] != board[row][col]:
                return False

            temp = board[row][col]
            board[row][col] = '*'
            for i in range(4):
                new_row = row + dir_x[i]
                new_col = col + dir_y[i]

                if helper(new_row, new_col, pos+1):
                    board[row][col] = temp
                    return True

            board[row][col] = temp
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]) and helper(i, j, 0):
                    return True
        
        return False
                    
        