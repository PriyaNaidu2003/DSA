class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        target=0
        for i in nums:
            if c==0:
                c,target=1,i
            elif i==target:
                c+=1
            else:
                c-=1
        return target
        
        