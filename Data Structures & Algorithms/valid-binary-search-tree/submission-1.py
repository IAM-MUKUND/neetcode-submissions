# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valiDIDDY(node, leftval, rightval):
            if not node:
                return True
            if not (node.val < rightval and node.val > leftval):
                return False
            
            return (valiDIDDY(node.left, leftval, node.val) and valiDIDDY(node.right, node.val, rightval))

        return valiDIDDY(root, float('-inf'), float('inf'))