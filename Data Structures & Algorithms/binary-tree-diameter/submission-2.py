# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxm_diameter = 0 

        def helper(root):
            nonlocal maxm_diameter 
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            maxm_diameter =  max(maxm_diameter, left + right)
            return 1 + max(left, right) #return height

        helper(root)

        return maxm_diameter 