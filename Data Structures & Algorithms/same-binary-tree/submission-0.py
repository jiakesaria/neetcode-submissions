# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        treep = deque([p]) 
        treeq = deque([q])

        while treep or treeq:
            for _ in range(len(treep)):
                nodep = treep.popleft()
                nodeq = treeq.popleft()

                if not nodep and not nodeq:
                    continue

                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False

                treep.append(nodep.left)
                treep.append(nodep.right)
                treeq.append(nodeq.left)
                treeq.append(nodeq.right)
 
        return True
        