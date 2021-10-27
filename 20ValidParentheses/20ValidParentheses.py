class Solution:
    def isValid2(self,s):
        temp = [] #initial the array to avoid index error

        for chr in s:
            val = temp[-1] if temp else '#'
            if self.Matched(val,chr):
                temp.pop()
            else:
                temp.append(chr)
        return (len(temp)==0)

    def Matched(self,s1,s2):
        matched = False
        if s1 == '(' and s2 ==')':
            matched = True
        if s1 == '[' and s2 ==']':
            matched = True
        if s1 == '{' and s2 =='}':
            matched = True
        return matched

if __name__ == '__main__':
    solution = Solution()
    s = "{[]}"
    print(solution.isValid2(s))