class Solution:
    def intersect(self, nums1, nums2):
        #Time O(m+n)
        #Space O(m+n)
        dict1 = {}
        dict2 = {}
        result = []
        for i in nums1:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in nums2:
            if i not in dict2.keys():
                dict2[i] = 1
            else:
                dict2[i] += 1

        keys_intersection = [key for key in dict1.keys() if key in dict2.keys()]
        print(keys_intersection)
        for key in keys_intersection:
            frequency = min(dict1[key],dict2[key])
            print(frequency,key)
            for k in range(frequency):
                result.append(key)
        return result

if __name__=='__main__':
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersect(nums1,nums2))