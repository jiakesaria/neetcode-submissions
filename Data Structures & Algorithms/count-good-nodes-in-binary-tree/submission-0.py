# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        def dfs(root, maxm):
            nonlocal count 
            if not root:
                return
            if root.val >= maxm:
                count += 1 
                maxm = root.val 
            dfs(root.left, maxm)
            dfs(root.right, maxm)
        dfs(root, root.val)
        return count 