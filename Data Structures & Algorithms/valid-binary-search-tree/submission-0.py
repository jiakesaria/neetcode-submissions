# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minm, maxm):
            if not root:
                return True #this path is over - all passed
            if not root.val > minm or not root.val < maxm:
                return False #can exit!
            #root is valid check its children 
            return (dfs(root.left, minm, root.val) and
            dfs(root.right, root.val, maxm))

        return dfs(root, float("-inf"), float("inf"))
