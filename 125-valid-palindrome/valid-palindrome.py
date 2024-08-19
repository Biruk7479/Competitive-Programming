class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                t=t+i.lower()
            else:
                pass           
        for i in range(len(t)//2):
            if t[i]!=t[-i-1]:
                return False
                break
        return True      
        