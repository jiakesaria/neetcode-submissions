class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        change = -1 #the first element of non rotated sorted array's index
        while l <= r:
            m = l + (r-l)//2 
            if nums[l] > nums[r]:
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            else:
                change = l 
                break 

        #picking one of the two sorted arrays
        if change == 0:
            l = 0
            r = len(nums) - 1
        else:
            if target < nums[0]:
                l = change
                r = len(nums) - 1
            elif target > nums[0]:
                l = 0
                r = change - 1
            else:
                return 0 # target == nums[0]
        
        #binary search on one of the sorted arrays
        while l <= r:
            m = l + (r-l)//2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m #target == nums[m]
        return -1