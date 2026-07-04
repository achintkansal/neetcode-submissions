# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def dfs(root):

            if root:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                res.append("N")
        
        dfs(root)
        result = ",".join(res)
        print(result)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(',')

        n = len(tree)

        self.pos = 0
        def construct_dfs():
            if self.pos >= n:
                return None
            
            if tree[self.pos] == 'N':
                return None
            
            root = TreeNode(val = int(tree[self.pos]))
            self.pos += 1
            root.left = construct_dfs()
            self.pos += 1
            root.right = construct_dfs()

            return root
        
        root = construct_dfs()
        return root
