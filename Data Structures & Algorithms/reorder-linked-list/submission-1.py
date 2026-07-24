# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        #slow currently at middle 
        #reverse list after the middle node
        curr = slow.next 
        slow.next = prev = None 
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr 
            curr = tmp 

        #2 pointers to merge 
        first = head 
        second = prev
        while second:
            tmp1 = first.next 
            first.next = second 
            tmp2 = second.next 
            second.next = tmp1
            first = tmp1
            second = tmp2
            
