class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for pair in edges:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
        print(adj_list)
        visited, cycle = set(), set()
        def find_cycle(prev, root):
            cycle.add(root)
            visited.add(root)
            for neig in adj_list[root]:

                if (prev != neig) and (neig in cycle):
                    return True
                # print(prev, root, neig)
                if (prev != neig) and find_cycle(root, neig):
                    return True
            
            cycle.remove(root)
            return False
        
        if find_cycle(-1, 0):
            return False
        if len(visited) != n:
            return False
        return True

        
