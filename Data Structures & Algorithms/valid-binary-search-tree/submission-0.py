# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def compare_nodes(lowerb, upperb, node):
            if not node:
                return True

            elif (lowerb >= node.val) or (upperb <= node.val):
                return False

            else:
                return compare_nodes(lowerb, node.val, node.left) and compare_nodes(node.val, upperb, node.right)

        return compare_nodes(float('-inf'), float('inf'), root)