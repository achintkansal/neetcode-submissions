class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## check row
        for i in range(9):
            check_set = set()
            for j in range(9):
                if (board[i][j] in check_set) and (board[i][j] != "."):
                    return False
                if board[i][j] != ".":
                    check_set.add(board[i][j])

        ## check column
        for i in range(9):
            check_set = set()
            for j in range(9):
                if (board[j][i] in check_set) and (board[j][i] != "."):
                    return False
                if board[j][i] != ".":
                    check_set.add(board[j][i])
        ## check boxes
        for square in range(9):
            check_set = set()
            for i in range(3):
                for j in range(3):
                    new_row = i + (square//3)*3
                    new_col = j + (square%3)*3
                    if board[new_row][new_col] == ".":
                        continue
                    if board[new_row][new_col] in check_set:
                        return False
                    check_set.add(board[new_row][new_col])        
        
        return True
        