class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0 
        elif len(s) == 1:
            return 1
        l = 0 
        r = 0 # l - r is the window 
        mp = defaultdict(int)
        length = 0
        maxf = 0
        while r < len(s) and l <= r: #substring can be len = 1
            mp[s[r]] += 1
            maxf = max(maxf, mp[s[r]]) #the character!
            while (r - l + 1) - maxf > k: #this substring is invalid
                length = max(length, r - l) 
                mp[s[l]] -= 1
                l += 1 #removing l               
            else:
                length = max(length, r - l + 1)
            r += 1 
        return length