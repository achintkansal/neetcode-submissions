# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []

        while len(queue) > 0:
            n = len(queue)
            curr_res = []
            for i in range(n):
                curr = queue.popleft()
                curr_res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            res.append(curr_res)
        return res