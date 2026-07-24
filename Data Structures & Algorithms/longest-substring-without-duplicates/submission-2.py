class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        length = 1 
        mp = {s[l] : 0}
        while r < len(s):
            #check for dupes using hasmap ? #O(1)
            if s[r] in mp and mp[s[r]] >= l:
                length = max(length, (r - l)) #not r - l + 1 because r is not part of the current substring because it is a dupe
                l = mp[s[r]] + 1 
                mp[s[r]] = r # new index     
            else:
                mp[s[r]] = r 
                length = max(length, (r - l + 1))
            r += 1 
        return length
        