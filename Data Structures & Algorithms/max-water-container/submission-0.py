class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        amt = 0
        for l in range(len(heights) - 1):
            r = l + 1
            while r < len(heights):
                curr = min(heights[l], heights[r]) * (r - l)
                amt = max(amt, curr)
                r += 1
        return amt 

        