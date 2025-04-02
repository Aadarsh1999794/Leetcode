import math
class Solution:
    def reverse(self, x: int) -> int:
        MIN=-2147483648
        MAX=2147483647
        rev=0
        pos=abs(x)
        while pos:
            rem = pos%10
            rev=((rev*10)+rem)
            pos=pos//10
        if rev>MAX or rev<MIN:
            return 0
        if x>0:
            rev=rev
        else:
            rev=rev*(-1)
        return rev
        