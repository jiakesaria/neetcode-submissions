# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # .val used to identify p and q
        # case 1 -- p can be q's ancestor -> answer is p and vice versa ; case 2 -- else the node where they split to right and left 
        # how do you remember where the two nodes are relative to each other? -- bst property
        # if p and q are on diff sides of root -> ans is root ; 
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root 
        if (p.val - root.val)*(q.val - root.val) < 0:
            return root 
        left = self.lowestCommonAncestor(root.left, p, q) # returns either none / root 
        if left:
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        return right 