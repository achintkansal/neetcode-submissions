# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## Assuming the Tree contains unique values only

        def check_same(p, q):
            if not p and not q:
                return True
            if not p or not q: 
                return False
            
            return ((p.val == q.val) and (check_same(p.left, q.left)) and (check_same(p.right, q.right)))
        
        def helper(root, subroot):
            if (root and subroot) and (root.val == subroot.val):
                return check_same(root, subroot) or helper(root.left, subroot) or helper(root.right, subroot)
            else:
                if root:
                    left = helper(root.left, subroot)
                    right = helper(root.right, subroot)

                    return (left or right)

                return False
        

        return helper(root, subRoot)
        