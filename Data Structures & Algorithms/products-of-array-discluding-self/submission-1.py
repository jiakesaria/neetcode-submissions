class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
            else:
                prod *= i
        output = [1] * len(nums)
        if zeroCount > 0:
           for i in range(len(nums)):
            if nums[i]!=0 or zeroCount > 1:
                output[i] = 0 
            else:
                output[i] = prod 
        else:
            for i in range(len(nums)):
                output[i] = prod//nums[i]
        return output
