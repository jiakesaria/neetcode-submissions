# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #res is list1
        prev = None
        curr1 = list1
        curr2 = list2
        res = None
        while curr1 and curr2:
            if curr2.val <= curr1.val:
                temp = curr2.next 
                if prev:
                    prev.next = curr2
                else:
                    res = curr2
                curr2.next = curr1
                prev = curr2
                curr2 = temp 
            else:
                if not prev:
                    res = curr1
                prev = curr1
                curr1 = curr1.next
        while curr2:
            if prev:
                prev.next = curr2
            else:
                res = curr2
            prev = curr2
            curr2 = curr2.next 
        while curr1:
            if prev:
                prev.next = curr1
            else:
                res = curr1
            prev = curr1
            curr1 = curr1.next
        return res     