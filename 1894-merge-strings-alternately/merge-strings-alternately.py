class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        x=len(word1)
        y=len(word2)
        if y>x:
            x=y
        for i in range(x):
           if (i != len(word1)) and (i != len(word2)):
             merged =merged + word1[i]
             merged =merged + word2[i]
           if i == len(word1):
             merged = merged + word2[i:]
             break
           elif i == len(word2):
             merged = merged + word1[i:]
             break
        return merged

        