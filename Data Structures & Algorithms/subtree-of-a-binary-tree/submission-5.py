# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(root):

            if not root:
                return '#'
            
            left = serialize(root.left)
            right = serialize(root.right)

            final_str = ('').join([str(root.val), left, right])
            return final_str
        
        root_str = serialize(root)
        subroot_str = serialize(subRoot)

        if subroot_str in root_str:
            return True
        else:
            return False

