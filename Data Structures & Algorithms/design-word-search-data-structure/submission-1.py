class TrieNode():
    def __init__(self):
        self.characters = [None] * 26
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        n = len(word)
        curr = self.root
        for i in range(n):
            pos = ord(word[i]) - ord('a')

            if curr.characters[pos]:
                curr = curr.characters[pos]
            
            else:
                curr.characters[pos] = TrieNode()
                curr = curr.characters[pos]

            if i == n-1:
                curr.eow = True

    def search(self, word: str) -> bool:
        n = len(word)
        def helper_dfs(curr_root, curr_pos):
            
            for i in range(curr_pos, n):
                pos = ord(word[i]) - ord('a')
                if word[i] == '.':
                    for j in range(26):
                        if curr_root.characters[j] and helper_dfs(curr_root.characters[j], i + 1):
                            return True
                    return False
                else:
                    if curr_root.characters[pos]:
                        curr_root = curr_root.characters[pos]
                    else:
                        return False
                
            return curr_root.eow
            
            
        
        return helper_dfs(self.root, 0)

        
