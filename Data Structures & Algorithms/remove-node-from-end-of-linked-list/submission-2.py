# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head 
        if not head.next:
            return None 
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next 
        remove = length - n + 1
        index = 1
        prev = None
        curr = head 
        while index <= remove:
            if index == remove:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next 
                break 
            else:
                prev = curr 
                curr = curr.next
                index += 1 
        return head 

        