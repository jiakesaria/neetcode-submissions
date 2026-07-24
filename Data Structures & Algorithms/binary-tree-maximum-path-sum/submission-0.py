# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxm = float("-inf")
        def helper(root): #return maxm path sum 
            nonlocal maxm 
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            local_max = max(left + root.val, right + root.val, root.val)
            maxm = max(local_max, maxm, left + right + root.val)
            return local_max
        helper(root)
        return maxm