class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = dict() #stores count of s 
        for i in s:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1 
        for j in t:
            if j in my_map:
               my_map[j] -= 1 
            else:
                return False 
        res = all(val == 0 for val in my_map.values())
        return res