class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        l=[]
        for i in digits:
            s+=str(i)
        s=str(int(s)+1)
        for i in s:
            l.append(int(i))
        return l
        
        

        