class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min cost to reach n from i 
        # cost[i] = cost to be on i 
        n = len(cost)
        dp = [0] * (n+3)
        #base case
        dp[n + 1] = dp[n + 2] = 0
        dp[n] = cost[n-1]
        for i in range(n-1, 0, -1):
            dp[i] = cost[i-1] + min(dp[i+1], dp[i+2])
        return min(dp[1], dp[2]) 
        