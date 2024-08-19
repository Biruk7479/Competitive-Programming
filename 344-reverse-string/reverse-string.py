from copy import deepcopy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        x=deepcopy(s)
        for i in range(len(s)):
            s[i]=x[-i-1]