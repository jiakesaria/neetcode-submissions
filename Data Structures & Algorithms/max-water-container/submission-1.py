class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        amt = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            amt = max(curr, amt)
            if heights[l] <= heights[r]:
                l += 1 
            else:
                r -= 1
        return amt 

        