class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for _ in range(len(nums) + 1)] #index is the frequency, value is num with that count 
        
        for val, c in count.items():
            freq[c].append(val) 

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n) #prob - freq[i] is list? doesnt it append the entire list? 
                if len(res) == k:
                    return res

        