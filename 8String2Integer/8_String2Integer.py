class Solution:
    MAX_VALUE = 2 ** 31 - 1
    MIN_VALUE = -2 ** 31

    def myAtoi(self, s: str) -> int:
        '''when the input s is not very long'''
        # remove the leading space
        s = s.strip(' ')  # .replace(' ', '')
        # # strip() removes space outside the string, replace(' ','') removes space inside the string
        sign = 1

        first_valid_sign = True
        valid_number = ''
        for i in s:
            if i in ['-', '+'] and first_valid_sign and len(valid_number) == 0:
                first_valid_sign = False
                sign = -1 if i == '-' else 1
            elif i.isdigit():
                valid_number += i
            else:
                break

        result = sign * int(valid_number) if valid_number.isdigit() else 0

        # clip the result
        result = max(min(result, self.MAX_VALUE), self.MIN_VALUE)

        return result

if __name__=='__main__':
    solver = Solution()
    y = '-3'
    print(float(y))

    import random
    x="++1"
    out = solver.myAtoi(x)
    print(out)