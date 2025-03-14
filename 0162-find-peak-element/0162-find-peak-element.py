class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        mindex=0
        if len(nums)==1:
            return 0
        elif nums[0]>nums[1]:
            mindex=0
        elif nums[len(nums)-1]>nums[len(nums)-2]:
            mindex=len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                mindex=i
        return mindex

        