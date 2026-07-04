class Node:
    def __init__(self,val):
        self.val = val
        self.adj = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hm = {}
            
        for pair in prerequisites:

            if pair[0] in hm:
                node1 = hm[pair[0]]
            else:
                hm[pair[0]] = Node(pair[0])
                node1 = hm[pair[0]]
            
            if pair[1] in hm:
                node2 = hm[pair[1]]
            else:
                hm[pair[1]] = Node(pair[1])
                node2 = hm[pair[1]]

            node2.adj.append(node1)
        
        visited = set()
        def find_cycle_dfs(root):

            visited.add(root)
            for neig in root.adj:

                if neig in visited:
                    return True
                
                if find_cycle_dfs(neig):
                    return True
            
            visited.remove(root)
            return False
        
        for key, val in hm.items():
            if find_cycle_dfs(val):
                print(key)
                return False
        
        return True

            

        