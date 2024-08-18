class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      d={}
      c={}
      for i in s:
        if i in d:
            d[i]+=1
        else: d[i] = 1    
      for i in t:
        if i in c:
            c[i]+=1
        else: c[i] = 1
      return d==c   

           
        