# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        flag=0
        size=len(nums)-1
        for i in range(len(nums)):
            if (target<= nums[i]):
                index=i
                break
            elif (target>nums[size]):
                index=size+1
                break
        return index
        
        
