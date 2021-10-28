class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp = []
        longest = 0
        pre_matched_index = -1

        for i,chr in enumerate(s):
            top = temp[-1] if temp else ('#',-1) # (val,index)
            if self.Matched(top[0],chr):
                length = i - top[1] + 1
                longest = longest if length<=longest else length # update the longest
                if i - pre_matched_index == 2:
                    longest += 2
                pre_matched_index = i
            else:
                temp.append((chr,i))

        return longest


    def Matched(self,s1,s2):
        matched = False
        if s1 =='(' and s2 == ')':
            matched = True
        return matched

if __name__=='__main__':
    solution = Solution()
    s = "))))"
    print(solution.longestValidParentheses(s))