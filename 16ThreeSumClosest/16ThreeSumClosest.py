import pdb
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        def threeSum(nums,possible):
            for i in range(len(nums)):
                # if nums[i] > possible:
                #     break
                if i == 0 or nums[i-1]!=nums[i]:
                    lo,hi = i+1,len(nums)-1
                    while (lo<hi):
                        sum = nums[i] + nums[lo] + nums[hi]
                        print(sum)
                        # pdb.set_trace()
                        if sum < possible:
                            lo += 1
                        elif sum > possible:
                            hi -= 1
                        else:
                            return [nums[i],nums[lo],nums[hi]]

        nums.sort()
        MIN = sum(nums[:3])
        MAX = sum(nums[-3:])
        answer = []
        if target >= MAX:
            return sum(nums[-3:])
        if target <= MIN:
            return sum(nums[:3])
        diffirence = 0
        while diffirence <= max(abs(MIN-target),abs(MAX-target)) and not answer:
            possible = target+diffirence
            answer = threeSum(nums,possible)
            if answer:
                break
            possible = target-diffirence
            answer = threeSum(nums, possible)
            diffirence += 1

        return sum(answer)

if __name__=='__main__':
    solver = Solution()
    x = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,\
         6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,\
         6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,\
         20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,\
         -4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
    target = -52
    output = solver.threeSumClosest(x,target)
    print(output)