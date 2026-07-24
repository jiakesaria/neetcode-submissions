import heapq 
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = k - 1
        maxheap = [(-nums[i], i) for i in range(r)] #of size k 
        heapq.heapify(maxheap) 
        res = []
        while r < len(nums):
            heapq.heappush(maxheap, (-nums[r], r)) #add new 
            while maxheap[0][1] < l: #remove from top thats why need indexto check if outside window, else deletion from centre takes log k 
                heapq.heappop(maxheap)
            maxm, indx = maxheap[0] #peek 
            res.append(-1 * maxm)
            l += 1
            r += 1 
        return res