# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(root) -> int:
            if root:
                l = find_height(root.left)
                r = find_height(root.right)
                root.val = 1 + max(l,r)
                return root.val
            return -1

        def helper(root) -> bool:
            if root:
                check_left = helper(root.left)
                check_right = helper(root.right)
                if not check_left or not check_right:
                    return False
                l = 1+root.left.val if root.left else 0
                r = 1+root.right.val if root.right else 0
                print(root.val)
                return True if abs(l - r) <= 1 else False
            
            return True
        find_height(root)
        return helper(root)


        