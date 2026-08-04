class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = number of ways to reach the top (n) starting from step i
        dp = [0] * (n + 2) # steps 1 to n , n + 1 for padding , ignore 0 
        # base case 
        dp[n] = 1
        dp[n + 1] = 0 
        #populate dp table!
        for i in range(n-1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]