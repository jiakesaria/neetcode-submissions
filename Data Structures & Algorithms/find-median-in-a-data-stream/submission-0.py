import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #first-half
        self.minHeap = [] #second-half    
        self.median = -1 #-1 placeholder!
    def addNum(self, num: int) -> None:
        
        if not self.maxHeap and not self.minHeap: #first 'addNum'
            heapq.heappush(self.minHeap, num)
        else:
            self.median = self.findMedian()
            if num <= self.median:
                if len(self.minHeap) >= len(self.maxHeap):
                    heapq.heappush(self.maxHeap, -num)
                else: #len(self.minHeap) < len(self.maxHeap):
                    heapq.heappop(self.maxHeap)
                    heapq.heappush(self.maxHeap, -num)
                    heapq.heappush(self.minHeap, self.median)
            else: #num > self.median
                if len(self.minHeap) <= len(self.maxHeap):
                    heapq.heappush(self.minHeap, num)
                else: #len(self.minHeap) > len(self.maxHeap):
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap, -self.median)
                    heapq.heappush(self.minHeap, num)  

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] + (-self.maxHeap[0]))/2
            
        elif len(self.minHeap) < len(self.maxHeap): 
            self.median = -self.maxHeap[0]
        else:
            self.median = self.minHeap[0]

        return self.median
        