#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
#Then return the number of unique elements in nums.

class Solution(object):
    def removeDuplicates(self, nums):
         index = 0
         for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

         return index + 1
        
