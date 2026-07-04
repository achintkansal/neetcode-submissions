class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.component = n
    
    def find_parent(self, a):

        if a != self.parent[a]:
            self.parent[a] = self.find_parent(self.parent[a])
        
        return self.parent[a]
    
    def union(self, a, b):
        da = self.find_parent(a)
        db = self.find_parent(b)

        if da == db:
            return False
        
        if self.size[da] < self.size[db]:
            da, db = db, da
        
        self.size[da] += self.size[db]
        self.parent[db] = da
        self.component -= 1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)

        for edge in edges:
            dsu.union(edge[0], edge[1])
        
        return dsu.component
        