# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter_func(root)
        return self.diameter
    def diameter_func(self, root: Optional[TreeNode]) -> int:  
        if root:
            l = self.diameter_func(root.left)
            r = self.diameter_func(root.right)
            h = 1 + max(l,r)
            self.diameter = max(self.diameter,l+r)
            return h
        else:
            return 0