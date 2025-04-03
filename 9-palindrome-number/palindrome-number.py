class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        comp=x
        if x<0:
            return False
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if rev==comp:
            return True
        else:
            return False
        