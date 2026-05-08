# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper_same_tree(p , q):

            if not p and not q:
                return True
            
            elif p and q:
                left = helper_same_tree(p.left, q.left)
                right = helper_same_tree(p.right, q.right)

                return left and right and (p.val == q.val)
            else:
                return False
        
        return helper_same_tree(p, q)
        