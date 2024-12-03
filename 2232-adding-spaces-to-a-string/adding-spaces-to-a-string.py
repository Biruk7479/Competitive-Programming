class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ls=""
        for i in range(len(spaces)):
            if i==0:
             ls += s[0:spaces[0]] + " "
            else:
             ls+=s[spaces[i-1]:spaces[i]] + " "
        ls += s[spaces[-1]:]
        return ls