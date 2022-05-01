class Solution:
    def calPoints(self, key):
        return self.valueDict[key] * key

    def deleteAndEarn(self, nums) -> int:
        from collections import Counter

        self.valueDict = dict(Counter(nums))

        keyList = list(self.valueDict.keys())
        keyList.sort()


        if len(keyList) == 1:
            return self.calPoints(keyList[0])

        if len(keyList) == 2:
            return max(self.calPoints(keyList[0]), self.calPoints(keyList[1])) if keyList[1] == keyList[0] + 1 else (
                        self.calPoints(keyList[1]) + self.calPoints(keyList[0]))

        print(keyList)
        dp = [0] * 3
        dp[0] = self.calPoints(keyList[0])
        dp[1] = max(dp[0], self.calPoints(keyList[1])) if keyList[1] == keyList[0] + 1 else (
                    self.calPoints(keyList[1]) + dp[0])

        for i in range(2, len(keyList)):
            dp[2] = max(dp[1], dp[0] + self.calPoints(keyList[i])) if keyList[i] == (keyList[i - 1] + 1) else (
                        dp[1] + self.calPoints(keyList[i]))
            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[2]