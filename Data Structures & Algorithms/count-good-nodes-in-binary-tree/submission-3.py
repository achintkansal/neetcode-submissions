# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def check_last_max(arr):
            return max(arr) == arr[-1]
        self.count = 0

        def helper(root, res):
            
            if root:
                res.append(root.val)
                
                if check_last_max(res):
                    self.count += 1
                helper(root.left, res) ## here result is call by ref not call by value
                helper(root.right, res)
                
                res.pop()

        helper(root, [])
        return self.count
        