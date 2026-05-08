# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ## using global variable
        self.diameter = 0
        def helper_diameter(root):
            
            if not root:
                return -1
            
            if not root.left and not root.right:
                return 0
            
            left = helper_diameter(root.left)
            right = helper_diameter(root.right)

            height = 1 + max(left, right)
            self.diameter = max(self.diameter, 2 + left + right)

            return height
        
        helper_diameter(root)
        return self.diameter

        