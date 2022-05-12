class Solution:
    def reverse(self, nums, j):
        start = j
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        j = len(nums) - 1
        i = j - 1

        while i >= 0:
            if nums[i] >= nums[j]:
                i -= 1
                j -= 1
            else:
                tmp = j
                # find the value just larger than the nums[i]
                while j < len(nums):
                    if nums[i] >= nums[j]:
                        break
                    j += 1

                nums[i], nums[j - 1] = nums[j - 1], nums[i]
                # reverse the sublist nums[tmp:]
                print(nums)
                self.reverse(nums, tmp)
                break
        else:
            self.reverse(nums, 0)