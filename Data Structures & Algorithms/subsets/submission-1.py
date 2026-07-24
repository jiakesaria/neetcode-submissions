class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1 << len(nums)): #2^n 
            subset = []
            for j in range(len(nums)): 
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
        