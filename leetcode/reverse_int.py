class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y = abs(x)
        while (y!=0):
            rem = y % 10 
            y = int(y/10)
            rev = rev*10 + rem
                
        if rev > -2147483648 and rev < 2147483647 :
            if x >= 0 :
                return rev
            else :
                return -rev
        else :
            return 0
