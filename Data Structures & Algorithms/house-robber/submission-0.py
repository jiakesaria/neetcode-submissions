class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = if i rob house i what is the max money i will get?
        # at dp[i] - only consider houses from i to n 
        n = len(nums)
        dp = [-1] * (n+2)
        #base case
        dp[n] = nums[n - 1] # at last house u can only consider robbing last house
        dp[n - 1] = nums[n - 2]
        dp[n + 1] = 0 
        for i in range(n-2, -1, -1):
            if i == 0:
                dp[i] = max([dp[j] for j in range(i + 1, n + 1)])
                break
            dp[i] = nums[i - 1] + max([dp[j] for j in range(i + 2, n + 1)])


        return dp[0]

        
        