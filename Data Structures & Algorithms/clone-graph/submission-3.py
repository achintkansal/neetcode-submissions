"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = set()
        mapping = {}

        def dfs(root):

            visited.add(root)

            for neighbour in root.neighbors:
                print(neighbour.val)
                if neighbour not in mapping:
                    mapping[neighbour] = Node(val = neighbour.val) 
                
                mapping[root].neighbors.append(mapping[neighbour])
                if neighbour not in visited:
                    dfs(neighbour)
        
        if not node:
            return node
        root = Node(val = node.val)
        mapping[node] = root

        dfs(node)

        return root

        