class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=""
        l=str(x)
        for i in range(len(l)):
            y=x%10
            s=s+str(y)
            x=x//10  
        if l == s:
            return True
        else:
            return False 
                