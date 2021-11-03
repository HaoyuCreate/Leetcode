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

    def merge2(self,nums1,m,nums2,n):
        # assume m =< len(nums1) and n <= len(nums2)
        if (not nums1) or m==0:
            nums1[:] = nums2
        elif (not nums2) or n==0:
            nums1[:] = nums1[:m]
        else:
            for i in range(len(nums1) - m):
                nums1.pop()
            for j in range(len(nums2) - n):
                nums2.pop()
            point1 = len(nums1)-1
            point2 = 0
            while point1>=0 and point2<n:
                print(point1,point2)
                if nums1[point1] <= nums2[point2]:
                    nums1.insert(point1+1,nums2[point2])
                    point2 += 1
                    point1 = m-1 + point2
                else:
                    point1 -= 1
        return nums1

    def merge3(self,nums1,m,nums2,n):
        # if (not nums1) or m==0:
        #     nums1[:] = nums2
        # elif (not nums2) or n==0:
        #     nums1[:] = nums1[:m]
        # else:
        #     for i in range(len(nums1) - m):
        #         nums1.pop()
        #     for j in range(len(nums2) - n):
        #         nums2.pop()
        point1 = m-1
        point2 = n-1
        point = m+n-1
        while point>=0 and point2>=0:
            if nums1[point1] > nums2[point2] and point1>=0:
                nums1[point] = nums1[point1]
                point1 = point1 - 1
                point -= 1
            else:
                nums1[point] = nums2[point2]
                point2 = point2 - 1
                point -= 1
        return nums1

if __name__=='__main__':
    solution = Solution()
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    print(solution.merge3(nums1,m,nums2,n))
