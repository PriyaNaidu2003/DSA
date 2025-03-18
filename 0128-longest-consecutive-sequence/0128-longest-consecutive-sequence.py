class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set=set(nums)
        c=0
        for i in num_set:
            if i-1 not in num_set:
                curr_num=i
                curr_streak=1
                while curr_num+1 in num_set:
                    curr_num+=1
                    curr_streak+=1
                c=max(c,curr_streak)
        return c
      
        

        