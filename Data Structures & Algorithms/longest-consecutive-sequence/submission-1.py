class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        res = 1 # len of longest sequence
        streak = 1 # currently for element at index 0
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i]+1:
                streak += 1
            else:
                streak = 1 #reset if next element breaks the subseq
            res = max(res, streak)
        return res    
            
            




        