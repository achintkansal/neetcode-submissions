class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = {}
        for i in range(numCourses):
            hm[i] = []
        
        visited = set()

        visited_overall = set()
        for pair in prerequisites:
            pair0 = pair[0]
            pair1 = pair[1]

            hm[pair1].append(pair0)
        
        dfs_stack = []
        self.isPossible = False ## contains cycle
        def topological_sort(root):

            visited.add(root)
            visited_overall.add(root)
            for neig in hm[root]:

                if neig in visited:
                    self.isPossible = True
                    continue
                
                topological_sort(neig)
                
            
            visited.remove(root)
            dfs_stack.append(root)


        for i in range(numCourses):

            if i not in visited_overall:
                topological_sort(i)
        
        if self.isPossible:
            return []
        res = dfs_stack[::-1]
        return res





        