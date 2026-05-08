# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def max_tree(root):
            if root:
                return max(root.val, max_tree(root.left), max_tree(root.right))
            return -1001
        
        def min_tree(root):
            if root:
                return min(root.val, min_tree(root.left), min_tree(root.right))
            return 1001
        if root:
            ans = (max_tree(root.left) < root.val) and (min_tree(root.right) > root.val)
            #print(ans, max_tree(root.left), min_tree(root.right))
            left = self.isValidBST(root.left)
            right = self.isValidBST(root.right)
            return (ans and left and right)
        else:
            return True    
                

        
    
        