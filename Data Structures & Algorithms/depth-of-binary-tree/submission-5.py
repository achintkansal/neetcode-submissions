# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         self.max_depth = 0
#         def helper_depth(root, depth):

#             self.max_depth = max(self.max_depth, depth)

#             if root:
#                 if root.left:
#                     helper_depth(root.left, depth+1)
#                 if root.right:
#                     helper_depth(root.right, depth+1)
#             else:
#                 self.max_depth = 0
                

#         helper_depth(root, 1)
#         return self.max_depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        def helper_depth(root):
            if not root:
                return 0
            
            left = helper_depth(root.left)
            right = helper_depth(root.right)

            max_depth = 1 + max(left, right)

            return max_depth

        ans = helper_depth(root)
        return ans
        
        
        