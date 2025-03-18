class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=1
        if 1 not in nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i]==1:
                if nums[i]==nums[i+1]:
                    c+=1
                else:
                    m=max(c,m)
                    c=1
            
        m=max(m,c)
        return m
        