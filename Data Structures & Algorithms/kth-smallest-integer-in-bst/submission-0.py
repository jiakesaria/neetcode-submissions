# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rank = 0 # 1-indexed 
        ans = 0
        found = False
        def dfs(root):
            nonlocal rank, ans, found
            if not root:
                return 
            #left before right
            dfs(root.left) 
            rank += 1 
            if rank == k:
                ans = root.val
                found = True
            if found:
                return
            dfs(root.right) #returns left child's rank

        dfs(root)

        return ans