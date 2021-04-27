class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10 == 0 and x!=0)):
            return False

        
        reverse = 0
        while (x > reverse):
            reverse= x%10 + reverse*10
            x = int(x/10)
            
        if (reverse == x or (int(reverse/10) == x)):
            return True
        else :
            return False
