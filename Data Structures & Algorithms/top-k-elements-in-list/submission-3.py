from collections import defaultdict
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = defaultdict(int)
        res = []
        for i in nums:
            freq[i] += 1
        for n, f in freq.items():
            heapq.heappush(heap, (-f, n))
        
        while k: 
            f, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res



        