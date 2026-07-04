class TrieNode:
    def __init__(self):
        self.characters = [None] * 26
        self.eow = False
        self.idx = -1


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str, idx: int) -> None:
        curr = self.root
        n = len(word)
        for i in range(n):
            pos = ord(word[i]) - ord("a")

            if curr.characters[pos]:
                curr = curr.characters[pos]
            else:
                curr.characters[pos] = TrieNode()
                curr = curr.characters[pos]

        curr.eow = True
        curr.idx = idx

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for i, word in enumerate(words):
            self.add_word(word, i)

        self.dir_x = [1, -1, 0, 0]
        self.dir_y = [0, 0, 1, -1]

        self.result = set()

        def helper(root, row, col, curr_res):
            curr = root
            if (
                row >= 0
                and col >= 0
                and row < len(board)
                and col < len(board[0])
                and board[row][col] != "*"
            ):
                pos = ord(board[row][col]) - ord("a")

                if curr.characters[pos]:
                    # curr_res.append(board[row][col])
                    temp = board[row][col]
                    board[row][col] = "*"
                    for d in range(4):
                        new_row = row + self.dir_x[d]
                        new_col = col + self.dir_y[d]

                        helper(curr.characters[pos], new_row, new_col, curr_res)

                    if curr.characters[pos].eow:
                        self.result.add(words[curr.characters[pos].idx])
                    # curr_res.pop()
                    board[row][col] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(self.root, i, j, [])
        return list(self.result)
