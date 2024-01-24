class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if (nums[i]==nums[j] and i!=j):
                   count=count+1
                   break
            if (count==0):
                break
        return nums[i]



       
        
