"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        queue_og = deque()
        queue_og.append(node)

        if not node:
            return None
        root = Node(val = node.val)
        
        visited = set() ## since the graph is undirected

        hm_map = {}
        hm_map[node] = root

        while len(queue_og) > 0:

            curr_node = queue_og.popleft()
            visited.add(curr_node.val)
            
            for neighbour in curr_node.neighbors:

                if neighbour.val not in visited:
                    queue_og.append(neighbour)
                    if neighbour not in hm_map:
                        new_node = Node(val = neighbour.val)
                        hm_map[neighbour] = new_node
                    else:
                        new_node = hm_map[neighbour]
                        
                    hm_map[curr_node].neighbors.append(new_node)
                    new_node.neighbors.append(hm_map[curr_node])
                    
        return root