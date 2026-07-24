class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1 
        while k>0:
            m = max(hashmap, key=hashmap.get)
            res.append(m)
            hashmap.pop(m)
            k -= 1 
        return res 
        