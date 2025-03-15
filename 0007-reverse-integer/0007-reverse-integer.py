class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        flag=False
        if '-' in str(x):
            x=x*(-1)
            flag=True
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x//=10
        if -2**31<rev and rev<((2**31)-1):
            if flag:
                return (rev*(-1))
            else:
                return rev
        else:
            return 0
        