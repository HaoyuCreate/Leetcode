class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp = []
        longest = 0
        final_longest = 0
        pre_matched_index = -2

        for i,chr in enumerate(s):
            top = temp[-1] if temp else ('#',-1) # (val,index)
            if self.Matched(top[0],chr):
                length = i - top[1] + 1
                longest = longest if length<=longest else length # update the longest in current valid group
                final_longest = final_longest if longest<=final_longest else longest #update the longest in the final
                if i - pre_matched_index == 2:
                    longest += 2
                pre_matched_index = i
                temp.pop()
            else:
                temp.append((chr,i))
                if chr != '(':
                    longest = 0 #recalculate the longest for a new valid group
            print(longest)
        return final_longest


    def longestValidParentheses2(self,s):
        temp = []
        length = 0
        longest = 0

        for i,chr in enumerate(s):
            if chr =='(' or not temp:
                temp.append(i)
            if chr ==')':
                index = temp.pop()
                length = i - index + 1
            longest = max(longest,length)
        return longest


    def longestValidParentheses3(self,s):
        stack = []
        dummy = '#'
        s = s+dummy
        max_group_len = sub_valid_len = curr_group_len = 0
        for index in range(len(s)):
            if not stack:
                sub_valid_len = sub_valid_len + curr_group_len
                curr_group_len = 0
                if s[index] == '(':
                    stack.append(s[index])
                else:
                    max_group_len = max(max_group_len,sub_valid_len)
                    sub_valid_len = 0
            else:
                if self.Matched(stack[-1],s[index]):
                    stack.pop()
                    curr_group_len += 2
                elif s[index]=='(':
                    stack.append(s[index])
                else:
                    max_group_len = max(max_group_len,sub_valid_len, curr_group_len)
            print(index,curr_group_len,sub_valid_len,max_group_len)

        return max_group_len

    def Matched(self,s1,s2):
        matched = False
        if s1 =='(' and s2 == ')':
            matched = True
        return matched

if __name__=='__main__':
    solution = Solution()
    s = "(()(((()"
    print('result=',solution.longestValidParentheses3(s))