class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window to len(s1) - fixed. hashmap to get characters and compare
        width = len(s1)
        s1map = defaultdict(int)
        for i in s1:
            s1map[i] += 1
        s2map = defaultdict(int) #stores characters in current windo
        l = 0
        r = width - 1
        for i in range(r): # l to r-1
            s2map[s2[i]] += 1 #initializing for the first window l to r
        while r < len(s2): #takes care of len(s1) > len(s2)
            s2map[s2[r]] += 1 # l to r
            if s1map == s2map:
                return True 
            else:
                s2map[s2[l]] -= 1
                if s2map[s2[l]] == 0:
                    del s2map[s2[l]]
                l += 1
                r += 1
                
        return False
        