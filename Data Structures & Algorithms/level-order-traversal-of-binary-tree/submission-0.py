# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## perform bfs append, popleft
        if not root:
            return []
        dq = deque()
        dq.append(root)
        ans = []
        length_of_level = len(dq)
        while length_of_level > 0:
            lst = []
            n = len(dq)
            print(dq)
            for j in range(n):
                element = dq.popleft()
                lst.append(element.val)
                if element.left:
                    dq.append(element.left)
                if element.right:
                    dq.append(element.right)
            ans.append(lst)
            length_of_level = len(dq)
        return ans
                

        