class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 1
        for n in nums:
            if (n-1) not in numSet: #to check if n is the starting pt.
                curr = n
                strk = 0
                while curr in numSet: #seq is being built
                    strk += 1
                    curr += 1 
                longest = max(longest, strk)
        return longest
            
            




        