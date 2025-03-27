class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i=0
        # if s=="":
        #     return True
        # for j in range(len(t)):
        #     if t[j]==s[i]:
        #         i+=1
        #         if i==len(s):
        #             break
        # return i==len(s)
        sp,tp=0,0
        while sp<len(s) and tp<len(t):
            if t[tp]==s[sp]:
                sp+=1
            tp+=1
        return sp==len(s)
        