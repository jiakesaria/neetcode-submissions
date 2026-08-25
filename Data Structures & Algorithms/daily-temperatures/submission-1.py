class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # search for the next warmer day - anamoly to monotonically decreasing stack 
        n = len(temperatures)
        res = [0] * n 
        stck = []

        for i in range(n):
            while stck and temperatures[i] > temperatures[stck[-1]]:
                idx = stck.pop()
                res[idx] = i - idx
            stck.append(i)

        return res
        