# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def find_idx(element):
            for i in range(len(inorder)):
                if inorder[i] == element:
                    return i

        self.preorder_idx = 0

        def helper(l, r):

            if l <= r:
                root = TreeNode(val = preorder[self.preorder_idx])
                inorder_idx = find_idx(root.val)
                self.preorder_idx += 1
                root.left = helper(l, inorder_idx-1)
                root.right = helper(inorder_idx+1, r)

                return root
            
            return None


        return helper(0, len(inorder)-1)