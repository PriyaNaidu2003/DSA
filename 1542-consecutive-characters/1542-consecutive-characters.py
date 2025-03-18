class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        m=0
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                m=max(c,m)
                c=1
        m=max(c,m)
        return m
       

        