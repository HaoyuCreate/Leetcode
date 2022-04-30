class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if len(cost) < 3:
            return min(cost[0], cost[1])

        dp = [0] * 3
        dp[0] = cost[0]
        dp[1] = cost[1]  # min(cost[0],dp[0]+cost[1]) if there is negtive value in cost

        # dp[i] = min(dp[i-2],dp[i-1]) + cost[i]
        # reach the top from index=len(cost)-1 or index=len(cost)-2

        for i in range(2, len(cost)):
            # dp[i] = min(dp[i-2],dp[i-1]) + cost[i]
            dp[2] = min(dp[0], dp[1]) + cost[i]
            dp[0] = dp[1]
            dp[1] = dp[2]

        return min(dp[0], dp[1])