class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split( )
        y=x[len(x)-1]
        z=len(y)
        return z

        