import math
class Solution:
    def reverse(self, x: int) -> int:
        NEG=0
        rev=0
        if x<0:
            NEG=1
            x=abs(x)        
        while x:
            rem = x%10
            rev=((rev*10)+rem)
            x=x//10
        if NEG==1:
            rev=rev*(-1)
            if rev<int(math.pow(-2,31)):
                return 0
            else:
                return rev
        else:
            if rev>math.pow(2,31):
                return 0
            else:
                return rev
        