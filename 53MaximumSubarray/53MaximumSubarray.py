class Solution:
    def maxSubArray(self, nums) -> int:
        max_sub = curr_sub = nums[0]
        for item in nums[1:]:
            curr_sub = max(item,item+curr_sub)
            max_sub = max(max_sub,curr_sub)
        return max_sub

    # two pointer method but has flaw
    def maxSubArray2(self, nums) -> int:
        fidx = 0
        sidx = 1

        if len(nums) < 2:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])

        max_sum = curr_sum = nums[0]

        while sidx < len(nums) + 1:
            curr_sum = sum(nums[fidx:sidx]) # sum(nums[head:tail]) is an O(n) method, not O(1)!!! nums[fidx:fidx+1] = nums[fidx]
            max_sum = max(max_sum,curr_sum)

            if curr_sum <= 0:
                # it is not matter if equalling to 0 when consider the maximum sum only,
                # but it is important to pick up the maximum length of subarrary as well as calculating the maximum sum
                fidx = sidx
                sidx += 1
                continue

            sidx += 1
        return max_sum

    # optmised two pointer method
    def maxSubArray3(self, nums) -> int:
        fidx = 0
        sidx = 1

        if len(nums) < 2:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])

        max_sum = curr_sum = nums[0]

        while sidx < len(nums) + 1:
            if curr_sum<=0:
                fidx = sidx
                curr_sum = nums[fidx]
                max_sum = max(curr_sum,max_sum)
                sidx += 1
                continue

            curr_sum = curr_sum+nums[sidx]
            max_sum = max(curr_sum,max_sum)
            sidx += 1
        return max_sum

if __name__=='__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray2(nums))

