# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-1001]
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                curr_node = (root.val + max(l, r, 0))
                res[0] = max(res[0] , (l + r + root.val),  curr_node) 
                print(res[0])   
                root.val = curr_node
                return curr_node
            return 0
        dfs(root)
        return res[0]
        