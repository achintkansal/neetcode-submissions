class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        n = len(word)
        
        curr = self.root
        for i in range(n):
            
            pos = ord(word[i]) - ord('a')
            curr_node = curr.nodes[pos]
            if curr_node:
                curr = curr_node
            else:
                curr.nodes[pos] = TrieNode()
                curr = curr.nodes[pos]

            if (i == n-1):
                curr.eow = True
 
    def search(self, word: str) -> bool:
        
        n = len(word)
        curr = self.root
        for i in range(n):
            curr_ch_pos = (ord(word[i]) - ord('a'))
            
            if not curr.nodes[curr_ch_pos]:
                return False

            curr = curr.nodes[curr_ch_pos]

            if (i == n-1) and not curr.eow: ## if the word is prefix
                return False
            
        
        return True

        
    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        curr = self.root
        for i in range(n):
            curr_ch_pos = (ord(prefix[i]) - ord('a'))
            if not curr.nodes[curr_ch_pos]:
                return False
            curr = curr.nodes[curr_ch_pos]
        
        return True