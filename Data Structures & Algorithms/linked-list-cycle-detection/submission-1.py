# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sp = head 
        fp = head 
        
        while True:
            sp = sp.next 
            if fp.next: #if next is a thing return 
                fp = fp.next.next 
            else:
                return False
            if sp == fp:
                return True
            elif fp is None:
                return False
