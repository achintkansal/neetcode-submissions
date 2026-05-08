# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left_range, right_range):
            if node:
                if node.val > left_range and node.val < right_range:
                    left = dfs(node.left, left_range, node.val)
                    right = dfs(node.right, node.val, right_range)
                    return (left and right)
                return False
            return True
        
        return dfs(root, -1001, 1001)
        