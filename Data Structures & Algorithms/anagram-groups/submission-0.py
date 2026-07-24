class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for word in strs:
            found = False 

            for grp in res: #compare to every grp  
                if sorted(grp[0]) == sorted(word):
                    grp.append(word)
                    found = True 
                    break 
            if not found:
                res.append([word])

        return res 
        