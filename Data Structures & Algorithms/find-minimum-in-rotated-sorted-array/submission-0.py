class Solution:
    def findMin(self, nums: List[int]) -> int:
        #rotation : bring last element first
        if len(nums) == 1:
            return nums[0]

        l = 0 
        r = len(nums) - 1
        
        while l < r:
            m = l + (r - l)//2
            if nums[l] > nums[r]: #happens in case of 1 to n-1 rotations
                if nums[m] > nums[r]:
                    l = m + 1
                else:#nums[m] < nums[r]
                    r = m 
            else:
                return nums[l]

        return nums[l]