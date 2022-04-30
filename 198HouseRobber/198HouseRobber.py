class Solution:
    def rob1(self, nums) -> int:
        # DP
        if len(nums) < 2:
            return nums[-1]
        dp = [0] * len(nums)  # dp[i] refers to the max robbering money at house i
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for house in range(2, len(nums)):
            dp[house] = max(dp[house - 1], dp[house - 2] + nums[house])

        return dp[-1]


    def rob2(self,nums):
        # DP + rolling array
        if len(nums) < 2:
            return nums[-1]
        if len(nums) < 3:
            return max(nums[0], nums[1])

        dp = [0] * 3
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[2] = max(dp[1], dp[0] + nums[i])
            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[2]

    def rob3(self,nums):
        # recursive + memory
        if not nums:
            return

        memo = {}

        def dp(nums, index):
            if index == 0:
                return nums[0]

            if index == 1:
                return max(nums[0], nums[1])

            if index not in memo:
                memo[index] = max(dp(nums, index - 1), dp(nums, index - 2) + nums[index])

            return memo[index]

        return dp(nums, len(nums) - 1)

    def rob4(self,nums):
        # recursive, very bad
        # O(2^n) time, O(n)
        if not nums:
            return

        def dp(nums, index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])

            return max(dp(nums, index - 1), dp(nums, index - 2) + nums[index])

        return dp(nums, len(nums) - 1)


sol = Solution()
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print(sol.rob2(nums))
print(sol.rob4(nums))