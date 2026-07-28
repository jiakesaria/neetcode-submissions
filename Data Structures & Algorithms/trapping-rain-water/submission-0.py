class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        prefix = [0] * len(height)
        maxm = height[0]
        for i in range(len(height)):
            if height[i] > maxm:
                maxm = height[i]
            prefix[i] = maxm
        suffix = [0] * len(height)
        maxm = height[len(height)-1]
        for i in range(len(height)-1, -1, -1):
            if height[i] > maxm:
                maxm = height[i]
            suffix[i] = maxm
        for i in range(1, len(height)-1): #first , last - empty 
            area += min(prefix[i], suffix[i]) - height[i]
        return area 
        