# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):

            if not root:
                return [True, 0]
            
            if not root.left and not root.right:
                return [True, 1]
            
            left = helper(root.left)
            right = helper(root.right)

            check_cond = (left[0]) and (right[0]) and (abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1], right[1])
            return [check_cond, height]
        res = helper(root)
        return res[0]
        