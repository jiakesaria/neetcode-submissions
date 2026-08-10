import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # in heap one no. per list w/ index so when popped that list next index is taken 
        heap = [] #(no., list no., next index)
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(heap, (lists[i].val, i, lists[i])) #len k 
        
        if not heap:
            return None

        dummy = ListNode(0)
        curr = dummy 

        while heap: 
            value, lis, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next 
            if node.next:
                heapq.heappush(heap,(node.next.val, lis, node.next))

        return dummy.next


        



        