class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = dict.fromkeys(nums, 0)
        for i in range(len(nums)):
            if my_map[nums[i]] == 0:
                my_map[nums[i]] = 1 
            else:
               return True
        return False 
        