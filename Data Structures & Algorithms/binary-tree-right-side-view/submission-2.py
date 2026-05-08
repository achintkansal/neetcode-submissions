# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        def helper(root, depth):
            if root:
                if depth > len(right_view):
                    right_view.append(root.val)
                
                helper(root.right, depth+1)
                helper(root.left, depth+1)

        helper(root, 1)
        return right_view
        