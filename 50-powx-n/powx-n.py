class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        mul=n
        if mul<0:
            mul=-1*mul
        while mul:
            if mul%2:
                ans=ans*x
                mul=mul-1
            else:
                x=x*x
                mul=mul/2
        if n<0:
            ans=1.0/ans
        return ans

        