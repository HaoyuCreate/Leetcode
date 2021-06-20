class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [];
        for i in range(len(nums)):
            first = nums[i]
            tmp = copy.copy(nums)
            tmp.remove(first)
            second = target - first
            if second in tmp:
                answer.append(nums.index(first))
                answer.append(tmp.index(second)+1)
                return answer
                break
        
        if len(answer)==0:
            print('target is not a sum of the numbers in the list')
            