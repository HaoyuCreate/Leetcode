class Solution:
    def countValue(self, n):
        # n>=1
        if n == 1:
            return None

        dp = [0] * 6
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2  # dp[2] + 1
        dp[5] = min(dp[2] + 1, dp[3] + 1)
        if n < 5:
            return dp[n]

        for i in range(5, n + 1):
            # dp[i] = min(dp[i-3]+1 + dp[i-2]+1)
            dp[5] = min(dp[2] + 1, dp[3] + 1)
            dp[2] = dp[3]
            dp[3] = dp[4]
            dp[4] = dp[5]
        return dp[-1]

    def minimumRounds(self, tasks) -> int:
        record = {}

        for task in tasks:
            if task not in record:
                record[task] = 1
            else:
                record[task] += 1

        rounds = 0
        memo = {}
        for key in record.keys():
            value = record[key]
            if value not in memo:
                memo[value] = self.countValue(value)
                if not memo[value]:
                    return -1
            rounds += memo[value]
        return rounds