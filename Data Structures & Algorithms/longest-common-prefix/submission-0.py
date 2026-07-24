class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            print(f"pref = {len(prefix)}")
            print(f"strs = {len(strs[i])}")
            if len(prefix) > len(strs[i]):
                prefix = prefix[:len(strs[i])] 
            for j in range(len(prefix)):
                    if strs[i][j] != prefix[j]:
                        prefix = prefix[:j]
                        break
        return prefix 