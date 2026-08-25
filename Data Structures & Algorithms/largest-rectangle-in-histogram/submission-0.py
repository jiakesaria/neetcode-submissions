class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # per i , we look next smallest on left n right , small is 
        # the anamoly -> strictly inc stack. create 2 stacks :
        # both ways -> & <- 
        n = len(heights)
        stck = [] 
        toright = [n] * n # toright[i] is the index of the next small height to i's right  
        toleft = [-1] * n # stores index 

        #first populate toright 
        for i in range(n): 
            while stck and heights[stck[-1]] > heights[i]: 
                idx = stck.pop()
                toright[idx] = i 
            stck.append(i)
        #populate toleft 
        stck = []
        for i in range(n-1, -1, -1): 
            while stck and heights[stck[-1]] > heights[i]: 
                idx = stck.pop()
                toleft[idx] = i
            stck.append(i)

        maxm = 0 
        for i in range(n): 
            area = heights[i] * (toright[i] - toleft[i] - 1)
            maxm = max(maxm, area)
        return maxm
        