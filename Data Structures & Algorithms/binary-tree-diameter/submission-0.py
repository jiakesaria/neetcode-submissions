# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        diam = left + right 

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        return max(diam, sub)

    def depth(self, node) -> int:
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
        