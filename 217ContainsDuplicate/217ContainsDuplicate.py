# Time complexity O(n)
# Space Complexty O(n)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        dict = {}
        for item in nums:
            if item not in dict.keys():
                dict[item] = 0
            else:
                return True
        return False

    def containsDuplicateBest(self, nums) -> bool:
        return len(set(nums)) != len(nums)

if __name__=='__main__':
    solution = Solution()
    list = [1,2,3]

    print(solution.containsDuplicate(list))