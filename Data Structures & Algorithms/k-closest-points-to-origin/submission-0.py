import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(-(math.sqrt(math.pow((point[0]-0), 2) + math.pow((point[1]-0), 2))), point) for point in points]
        #key is -ve of Euclidean distance between points[i] and (0,0), val is points[i]

        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        #now heap contains k closest points to the origin (0, 0).

        res = []
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])
        return res