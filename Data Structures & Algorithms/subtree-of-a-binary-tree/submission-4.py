# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p , q):

            if not p and not q:
                return True
            
            elif p and q:
                left = same_tree(p.left, q.left)
                right = same_tree(p.right, q.right)

                return left and right and (p.val == q.val)
            
            else:
                return False
        
        def helper_issubtree(root, subroot):

            if not root:
                return False

            if (root.val == subroot.val) and same_tree(root, subroot):
                return True
            
            else:
                left = helper_issubtree(root.left, subroot)
                right = helper_issubtree(root.right, subroot)

                return (left or right)
        
        return helper_issubtree(root, subRoot)    
                
        