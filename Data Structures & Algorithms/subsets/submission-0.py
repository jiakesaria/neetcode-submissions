class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for j in res[:]: #[:] - snapshot
                res.append(j + [i])
        return res
        