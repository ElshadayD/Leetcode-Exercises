# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def isPalindrome(self, x):
        reversed=0
        original=x
        if(x<0):
            x=x*-1
        while(x>0):

            reversed=(reversed*10)+(x%10)
            x=x/10
        if(original!=reversed):
            return False
        
        
        return True


 


      
        
