import math
class Solution:
    def reverse(self, x: int) -> int:
        NEG=0
        rev=0
        if x<0:
            NEG=-1
        else:
            NEG=1
        x=abs(x)
        while x>0:
            rem = x%10
            rev=((rev*10)+rem)
            x=x//10
        rev=NEG*rev
        if rev>=(-2**31) and rev<=(2**31)-1:
            return rev
        return 0
        