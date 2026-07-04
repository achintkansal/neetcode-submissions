class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        ## create adj list (graph)
        adj_list = {}
        adj_list[beginWord] = set()

        for word in wordList:
            adj_list[word] = set()
        
        def find_distance(word1, word2):
            n = len(word1)
            dis = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    dis += 1
            
            return dis
        
        wordList.append(beginWord)
        n = len(wordList)
        for i in range(n):
            for j in range(n):
                if find_distance(wordList[i], wordList[j]) == 1:
                    adj_list[wordList[i]].add(wordList[j])
                    adj_list[wordList[j]].add(wordList[i])
                    
        print(adj_list)
        ## do bfs to find shortest distance on undirected graph
        visited = set()
        queue = deque()
        queue.append(beginWord)

        dist = 0
        while len(queue) > 0:
            
            n = len(queue)
            
            for i in range(n):
                curr = queue.popleft()
                visited.add(curr)
                if curr == endWord:
                    return dist + 1

                for neigh in adj_list[curr]:
                    if neigh not in visited:
                        queue.append(neigh)
            dist += 1

        return 0
        