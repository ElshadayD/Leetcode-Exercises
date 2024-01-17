
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        temp= [0 for x in range(2)]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    temp[0]=i
                    temp[1]=j
                    break
        return temp

      
