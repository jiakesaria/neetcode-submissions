class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # first finish - greedy aproach when it comes to removing overlapping intervals
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev: 
                res += 1
                prev = min(prev, end)
            else: 
                prev = end 
        return res 