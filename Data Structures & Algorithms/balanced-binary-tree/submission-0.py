# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def heightree(root):
            if root is None:
                return 0

            return 1 + max(heightree(root.left), heightree(root.right))
    
        if root is None:
            return True
    
        left_height = heightree(root.left)
        right_height = heightree(root.right)
        
        r_balanced = self.isBalanced(root.right)
        l_balanced = self.isBalanced(root.left)
        
        if (r_balanced and l_balanced) and (left_height - right_height in [-1,0,1]):
            return True
        
        else:
            return False