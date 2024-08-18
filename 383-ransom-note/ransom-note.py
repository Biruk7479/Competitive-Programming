class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1    
            
        val=True   
        for j in ransomNote:
            if j in d and d[j]!=0:
                 d[j]-=1
            else:
                val = False         
        return val    