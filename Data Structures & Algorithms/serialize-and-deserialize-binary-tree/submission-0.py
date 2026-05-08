# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root:
            l = self.serialize(root.left)
            r = self.serialize(root.right)
            curr = f"{root.val}$" + l + r
            return curr
        return "n$"

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        tree_list = data.split("$")[:-1]
        print(tree_list)
        n = len(tree_list)
        i = [0]
        def helper(tree_list):
            if i[0] < n:
                char = tree_list[i[0]]
                print(i[0])
                if char != 'n':
                    node = TreeNode(int(char))
                    i[0] = i[0] + 1
                    node.left = helper(tree_list)
                    i[0] = i[0] + 1
                    node.right = helper(tree_list)
                    return node
                return None
            return None

        return helper(tree_list)
