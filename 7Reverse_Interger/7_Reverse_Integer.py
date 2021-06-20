class Solution:
    def reverse(self, x: int) -> int:
        assert isinstance(x,int), 'Invaild input'
        threshold = 2**31
        if x < (-threshold) or x > (threshold-1):
            return 0
        tmp = list(str(abs(x)))
        tmp = tmp[::-1]
        new=str()
        if x == 0:
            return 0
        else:
            out = int((x/abs(x)) * int(new.join(tmp)))
        if out < (-threshold) or out > (threshold-1):
            return 0
        return out


if __name__=='__main__':
    solver = Solution()
    import random
    x = 0
    out = solver.reverse(x)
