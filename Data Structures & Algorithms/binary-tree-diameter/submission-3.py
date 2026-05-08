# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def helper(root):

            if not root:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)

            self.diameter = max(self.diameter, left_height + right_height)

            height = 1 + max(left_height, right_height)
            return height
        
        helper(root)
        return self.diameter

        