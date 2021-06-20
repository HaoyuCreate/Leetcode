class Solution:
    def myAtoi(self, s: str) -> int:
        '''when the input s is not very long'''
        import re
        threshold = 2 ** 31
        s = s.strip(' ')  # .replace(' ', '')
        # # strip() removes space outside the string, replace(' ','') removes space inside the string

        # if s is None:
        #     return 0

        # s = re.sub(r'[^0-9+-]', '.', s) # turn all alphabet into '.'
        # string_list = s.split('.')
        # tmp = string_list[0]
        # # re.split(r'[+-]{2,}' split the sting by more than one '+' or '-', i.e '++++' and '--')
        # # re.sub(r'\D'$,'') remove all non-digits from the bottom
        # # out = re.sub(r'([\D])$','',re.split(r'[+-]{2,}',tmp)[0])
        # tmp = re.split(r'^[+-]*',tmp)
        # print(tmp)
        tmp = re.findall(r'(^[+]{0,1}\d+)|(^[-]{0,1}\d+)',s)
        if not tmp:
            return 0
        else:
            out = tmp[0][0] if tmp[0][0]!='' else tmp[0][1]
        out = int(float(out))
        # if out > threshold - 1:
        #     out = threshold - 1
        # elif out < -threshold:
        #     out = -threshold
        return max(-2**31,min(out,2**31-1))

if __name__=='__main__':
    solver = Solution()
    y = '-3'
    print(float(y))

    import random
    x="++1"
    out = solver.myAtoi(x)
    print(out)