# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        ans = [0]
        def inorder(root, k):
            if root:
                if k >= count[0]:
                    inorder(root.left, k)
                    count[0] += 1
                    if k == count[0]:
                        ans[0] = root.val
                        count[0] += 1
                        return ans[0]
                    inorder(root.right, k)
            return ans[0]
        return inorder(root,k)


        
        
        