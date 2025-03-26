class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in candies:
            flag=False
            for j in candies:
                if j==i:
                    continue
                else:
                    if i+extraCandies>=j:
                        flag=True
                    else:
                        flag=False
                        
                        break
            l.append(flag)
        return l
        