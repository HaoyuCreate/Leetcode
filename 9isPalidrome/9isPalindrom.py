class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            strx = list(str(x))
            start=0
            end=len(strx)-1
            while start<end:
                if strx[start] != strx[end]:
                    return False
                start+=1
                end-=1
            return True
        except(ValueError, ArithmeticError):
            print('Invalid input')