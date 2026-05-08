# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        lst = []
        if not root and not subRoot:
            return True
        def find_subroot_in_root(root, subroot):
            if root:
                find_subroot_in_root(root.left,subroot)
                find_subroot_in_root(root.right,subroot)
                if root.val == subroot:
                    lst.append(root)

            return None
        if root and subRoot:    
            start = find_subroot_in_root(root,subRoot.val)
        else:
            return False
        def check_tree(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot:
                if root.val == subroot.val:
                    l = check_tree(root.left,subroot.left)
                    r = check_tree(root.right, subroot.right)
                    return (l and r)
                return False
            return False
        print(lst)
        for root_start in lst:
            check = check_tree(root_start,subRoot)
            if check: return True

        return False
        