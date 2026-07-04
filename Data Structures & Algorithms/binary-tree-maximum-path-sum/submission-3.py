# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = -1001
        def helper_max_sum(root):

            if root:
                
                left = max(helper_max_sum(root.left), 0)
                right = max(helper_max_sum(root.right), 0)

                self.max_sum = max(self.max_sum, root.val + left + right)

                curr_path_max = root.val + max(left, right, 0)
                return curr_path_max
            
            return 0

        helper_max_sum(root)
        return self.max_sum