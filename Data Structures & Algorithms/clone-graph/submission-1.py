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

        clone_adj = []

        queue_og = deque()
        queue_clone = deque()

        queue_og.append(node)

        if not node:
            return None
        root = Node(val = node.val)
        queue_clone.append(root)
        hashset = set() ## since the graph is undirected

        hm_map = {}
        hm_map[node] = root

        while len(queue_og) > 0:
            curr_node = queue_og.popleft()
            hashset.add(curr_node.val)
            curr_node_clone = queue_clone.popleft()

            for neighbour in curr_node.neighbors:

                if neighbour.val not in hashset:

                    queue_og.append(neighbour)

                    if neighbour not in hm_map:
                        new_node = Node(val = neighbour.val)
                        hm_map[neighbour] = new_node

                    else:
                        new_node = hm_map[neighbour]
                        
                    curr_node_clone.neighbors.append(new_node)
                    new_node.neighbors.append(curr_node_clone)

                    queue_clone.append(new_node)
                    

        
        return root