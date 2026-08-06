class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # dp[i] = min number of intervals to remove to make all non-overlapping
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