# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lst1 = []
        lst2 = []
        def helper_func(root, p, lst):
            if root:
                if root.val == p.val:
                    lst.append(root)
                    return
                if p.val < root.val:
                    helper_func(root.left, p, lst)
                else:
                    helper_func(root.right, p, lst)

                lst.append(root)
        
        helper_func(root, p, lst1)
        helper_func(root, q, lst2)

        min_len = min(len(lst1), len(lst2))
        for i in lst1:
            for j in lst2:
                if i.val == j.val:
                    return i
        
        return root



        