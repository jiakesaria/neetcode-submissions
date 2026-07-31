"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: #edge case -- empty node
            return None
        root = Node(node.val)
        #hmap - value : deep_copy_node
        hmap = {node.val: root}
        #queue - (og node, deep copy node)
        q = deque([(node, root)])        
        while q:
            for _ in range(len(q)):
                nodes = q.popleft()                  
                for i in nodes[0].neighbors:
                    if i.val not in hmap:
                        hmap[i.val] = Node(i.val) #temp
                        q.append((i, hmap[i.val])) # appends og nodes
                    nodes[1].neighbors.append(hmap[i.val])
        return root
        