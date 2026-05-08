# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def find_height(root):
            if root:
                check_left_subtree, height_left_subtree = find_height(root.left)
                check_right_subtree, height_right_subtree = find_height(root.right)
                
                return [((check_left_subtree) and (check_right_subtree) and
                abs(height_left_subtree - height_right_subtree) <= 1),
                 1 + max(height_left_subtree,height_right_subtree)]
            return [True, 0]

        return find_height(root)[0]
