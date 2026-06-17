# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def heightree(root):
            if root is None:
                return 0

            return 1 + max(heightree(root.left), heightree(root.right))
    
        if root is None:
            return True
    
        left_height = heightree(root.left)
        right_height = heightree(root.right)

        islb = self.isBalanced(root.left)
        islr = self.isBalanced(root.right)

        if (left_height - right_height in [-1,0,1]) and (islb and islr):
            return True
        
        else:
            return False