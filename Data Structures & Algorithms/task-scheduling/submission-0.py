import heapq 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = defaultdict(int) #key is A-Z, value is freq 
        for i in tasks:
            hashMap[i] += 1
        maxHeap = [(-freq, alphabet) for alphabet, freq in hashMap.items()]
        heapq.heapify(maxHeap)
        cycles = 0 
        pending = deque() #k-length queue 
        while maxHeap or pending: #either one exists

            cycles += 1

            if pending and pending[0][1] <= cycles: #after k cycles add curr back to maxHeap
                c = pending.popleft()
                heapq.heappush(maxHeap, c[0]) 
            if maxHeap:
                curr = heapq.heappop(maxHeap) #curr is (-freq, alphabet)
                if curr[0] < -1: #else freq currently is 0 -- all processed
                    curr1 = (1 + curr[0], curr[1])
                    pending.append((curr1, cycles + n + 1))
 
        return cycles