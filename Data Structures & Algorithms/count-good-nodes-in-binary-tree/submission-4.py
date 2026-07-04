# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        def helper(root, _max):
            
            if root:
                if root.val >= _max:
                    self.count += 1
                    _max = root.val

                helper(root.left, _max)
                helper(root.right, _max)
                
        _max = -101 # check constraints... min value is -100
        helper(root, _max)
        return self.count
        