import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for i in nums: #O(n)
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1 
        heap = [(-count, num) for num, count in hashmap.items()] #list with key-value pair , only min-heap possible in python
        heapq.heapify(heap) #list -> heap

        while k>0: #O(k*n) ; k linear searches 
            c, v = heapq.heappop(heap)
            res.append(v)
            k -= 1 
        return res 
        