# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        diameter = self.height(root.left) + self.height(root.right)
        root.val = diameter

        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        
        
        return max(diameter,l,r)         



    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # if root.left == None and root.right == None:
        #     return 0
        if root:
            return 1+max(self.height(root.left), self.height(root.right))
        

        