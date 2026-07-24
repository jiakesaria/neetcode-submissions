class Solution:

    def encode(self, strs: List[str]) -> str:

        st = ""
        for s in strs:
            st = st + str(len(s)) + '#' + s
        return st 

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i<len(s):
            sl = '' #new len per string 
            while s[i]!='#':
                sl += s[i]
                i += 1 
            l = int(sl) #contains length, currently i is at '#'
            curr = s[i+1 : i+1+l] #excludes i+1+l
            res.append(curr)
            i = i+1+l
        return res
