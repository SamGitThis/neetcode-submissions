# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        md = 0
        def height(tree):
            nonlocal md
            if tree is None:
                return 0

            l = height(tree.left)
            r = height(tree.right)

            md = max(l+r, md)

            return 1 + max(height(tree.left), height(tree.right))

        height(root)

        return md



