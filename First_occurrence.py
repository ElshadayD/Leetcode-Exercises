
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
     
        if needle=="":
          return 0;
        else:

            for i in range(len(haystack)):
                if(haystack[i]==needle[0]):
                    if(haystack[i:i+len(needle)]==needle):
                       return i
            return -1
