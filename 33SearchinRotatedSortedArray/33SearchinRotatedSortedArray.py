class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        start = end = -1
        # with rotation nums[l] > nums[r]
        # with no rotaton, nums[l] < nums[r]

        while l <= r:
            mid = int((l + r) // 2)
            if mid == l:
                break
            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                #  no rotation
                break
            elif nums[l] > nums[mid] and nums[mid] > nums[r]:
                # impossible, invalid inputs
                pass
            elif nums[l] < nums[mid] and nums[mid] > nums[r]:
                l = mid
            else:
                # nums[l] > nums[mid] and nums[mid] < nums[r]
                r = mid

        start = r
        l1 = nums[:start]
        l2 = nums[start:]

        k1 = self.Bisearch(l1, target)
        k2 = self.Bisearch(l2, target)

        if k2 != -1:
            k2 = len(l1) + k2

        return max(k1, k2)

    def Bisearch(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return -1


