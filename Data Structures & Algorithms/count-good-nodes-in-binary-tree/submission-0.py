# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_path = -101
        count = [0]
        def helper(root, max_path):
            
            if root:
                if root.val >= max_path:
                    count[0] += 1
                    max_path = root.val
                helper(root.left, max_path)
                helper(root.right, max_path)
        helper(root, max_path)
        return count[0]

        