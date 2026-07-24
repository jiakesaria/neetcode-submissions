# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:  #subRoot is there 
            return False
        def isSameTree(root, subroot):
            if not root and not subroot:
                return True 
            elif not root or not subroot:
                return False 
            if root.val == subroot.val:
                return isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)
            else:
                return False
        def answer(root, subroot):
            if not root and not subroot:
                return True 
            elif not root or not subroot:
                return False 
            if root.val == subroot.val:
                ans = isSameTree(root, subroot)
                if ans:
                    return True 
                else:
                    return answer(root.left, subroot) or answer(root.right, subroot)            
            else:
                return answer(root.left, subroot) or answer(root.right, subroot)
        return answer(root, subRoot)
