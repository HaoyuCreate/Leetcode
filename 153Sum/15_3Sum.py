class Solution:
    def threeSum(self, nums):#: List[int]) -> List[List[int]]:
        '''O(N!/[(N-3)!3!])'''
        if len(nums)>3000 or len(nums)<1: return []
        if max(nums)>=10**5 or min(nums)<=-10**5: return []

        def match_principle(i,j,k):
            return i+j+k==0

        index_list = list(range(len(nums)))
        all_possible = []
        for i in index_list:
            for j in index_list:
                for k in index_list:
                    one_possible = {i,j,k}
                    if len(one_possible) != 3:
                        continue
                    else:
                        one_possible = list(one_possible)
                        x,y,z = one_possible
                        if match_principle(nums[x],nums[y],nums[z]):
                            one_collection = sorted([nums[x],nums[y],nums[z]])
                            # print('index',(x,y,z))
                            # print(one_collection,'\n')
                            if one_collection not in all_possible:
                                all_possible.append(one_collection)
        return all_possible

    def threeSum2(self,nums):
        '''O(N!/[(N-3)!3!])'''
        if len(nums) > 3000 or len(nums) < 1: return []
        if max(nums) >= 10 ** 5 or min(nums) <= -10 ** 5: return []
        def match_principle(i, j, k):
            return i + j + k == 0
        all_possible=[]

        from itertools import combinations
        for one_possible in combinations(nums,3):
            x, y, z = one_possible
            if match_principle(x, y, z):
                if sorted([x,y,z]) not in all_possible:
                    all_possible.append(sorted([x,y,z]))
        return all_possible

    def threeSum3(self,nums):
        '''O(n^2)'''
        if len(nums) > 3000 or len(nums) < 1: return []
        if max(nums) >= 10 ** 5 or min(nums) <= -10 ** 5: return []
        def match_principle(i, j, k):
            return i + j + k == 0
        all_possible=[]
        index_list = list(range(len(nums)))
        for i in index_list:
            first = nums[i]
            for j in index_list:
                if j != i:
                    second = nums[j]
                    possile_third = - (first + second)

                    indices = [k for k, element in enumerate(nums) if element == possile_third and k != i and k != j]
                    if not indices:
                        continue
                    else:
                        third = nums[indices[0]]
                    one_possible = sorted([first,second,third])
                    if third in nums and one_possible not in all_possible:
                        all_possible.append(one_possible)

        return all_possible

    def threeSum4(self,nums):
        import copy
        index_list = list(range(len(nums)))
        all_possible = []

        def twoSum(new_nums,first_rest,all_possible):
            for j in range(len(new_nums)):
                second = new_nums[j] #second = 2
                tmp = copy.copy(new_nums)
                tmp.pop(j) #tmp=[-1,0,1,-1]
                # print(-first_rest,new_nums,second,tmp)
                third = first_rest - second
                if third in tmp and sorted([-first_rest,second,third]) not in all_possible:
                    all_possible.append(sorted([-first_rest,second,third])) #ans=[], ans=[x1,x2],ans=[[z,x1,x2],[y1,y2]]
            return all_possible

        for i in index_list:
            first = nums[i] # t = -4
            first_rest = -first
            new_nums = copy.copy(nums)
            new_nums.pop(i) # [-1,0,1,2,-1]
            twoSum(new_nums,first_rest,all_possible) #ans=[],ans=[[x1,x2],ans=[[x1,x2],[y1,y2]]]
        return all_possible


if __name__=='__main__':
    solver = Solution()
    x =  [-1,0,1,2,-1,-4]
    # x = [3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]
    out = solver.threeSum4(x)
    print(out)