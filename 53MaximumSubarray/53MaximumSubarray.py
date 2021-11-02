class Solution:
    def maxSubArray(self, nums) -> int:
        max_sub = curr_sub = nums[0]
        for item in nums[1:]:
            curr_sub = max(item,item+curr_sub)
            max_sub = max(max_sub,curr_sub)

        return max_sub


if __name__=='__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))

