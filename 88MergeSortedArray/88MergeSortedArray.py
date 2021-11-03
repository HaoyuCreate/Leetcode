class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - m):
            nums1.pop()
        for j in range(len(nums2) - n):
            nums2.pop()
        nums1.extend(nums2)
        nums1.sort()
        return nums1


if __name__=='__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(solution.merge(nums1,m,nums2,n))
