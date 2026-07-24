class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)): #fix 1
            if nums[i] > 0: #3 +ve numbers cannot sum upto 0
                break 
            if i > 0 and nums[i-1] == nums[i]:
                continue #skip this iteration 
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 #there can be more triplets containing nums[i]
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1 #move left to lower the sum 
                else:
                    l += 1 #move right to increase the sum 

        return res


        