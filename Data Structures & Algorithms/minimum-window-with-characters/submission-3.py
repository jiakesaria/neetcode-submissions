class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = defaultdict(int)
        for i in t: #mapping characters of t 
            tmap[i] += 1 

        l = r = 0
        smap = defaultdict(int)
        res = '' 
        while r < len(s):
            smap[s[r]] += 1

            while all(smap[k] >= v for k, v in tmap.items()):               
                if (s[l] not in tmap or smap[s[l]] > tmap[s[l]]):  # is window still valid 
                    smap[s[l]] -= 1
                    l += 1
                else:     
                    curr = s[l:r+1]
                    if not res or len(curr) < len(res):
                        res = curr #return the shortest substring

                    smap[s[l]] -= 1
                    l += 1 #new substring begins 

            r += 1 
        return res 