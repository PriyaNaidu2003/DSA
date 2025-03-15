class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        dic={}
        for i,ele in enumerate(nums):
            complement=target-ele
            if complement in dic:
                return [dic[complement],i]
            dic[ele]=i
        
        