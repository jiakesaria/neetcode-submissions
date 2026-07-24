# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 , n2 = l1 , l2
        num1 = ''
        num2 = ''
        while n1:
            num1 += str(n1.val)
            n1 = n1.next 
        numb1 = int(num1[::-1])
        while n2:
            num2 += str(n2.val)
            n2 = n2.next
        numb2 = int(num2[::-1])

        #numb1 and numb2 need to be reversed 

        lsum = numb1 + numb2

        dig = lsum%10
        lsum = lsum//10
        head = prev = ListNode(dig)

        while lsum:
            dig = lsum%10
            lsum = lsum//10
            tmp = ListNode(dig)
            prev.next = tmp 
            prev = tmp

        return head  